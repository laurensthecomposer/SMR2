from ui_main_window import Ui_MainWindow
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys, time
import machine_controller_test as machine_controller
import numpy as np
bolt_sorter_machine = machine_controller.MachineController()

from cv2 import cv2
import ueye_camera

class MachineThread(QThread):
    first_run = True
    BoltFrame = Signal(np.ndarray)
    BoltType = Signal(str)
    BoltCounts = Signal(list)

    def stop_machine(self):
        bolt_sorter_machine.machine_stop()
        self.quit()

    def run(self):
        print("====== begin run")
        if self.first_run:
            bolt_sorter_machine.data_startup()
            bolt_sorter_machine.machine_startup()

            self.first_run = False

        bolt_sorter_machine.belts_roll()

        # timer = QTimer()
        # timer.setSingleShot(True)
        # timer.connect(bolt_sorter_machine.machine_startup)
        # timer.connect(self.terminate())
        # # timer.start(int(1000*60*3)) # timeout after 3 minutes
        # timer.start(3000) # test
        # # start timer
        # # if timer then stop machine and stop thread
        while not bolt_sorter_machine.lightgate(): # wait until bolt detected
            continue
        # timer.stop()

        # reset timer
        bolt_sorter_machine.img_stop()
        ret, frame = bolt_sorter_machine.img_capture()
        self.BoltFrame.emit(convertCv2ToQt(frame))

        bolt_sorter_machine.img_save(frame)

        bolt_type, pred, bolt_code, counts = bolt_sorter_machine.img_classify(frame)

        self.BoltType.emit(bolt_type)
        self.BoltCounts.emit(counts)

        bolt_sorter_machine.exit_classified_bolt()
        bolt_sorter_machine.robot_drop(bolt_type)




class CameraThread(QThread):
    changePixmap = Signal(QImage)

    def run(self):
        # cap = ueye_camera.UeyeCameraCapture(1)
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 512, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

def convertCv2ToQt(frame):
    rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    h, w, ch = rgbImage.shape
    bytesPerLine = ch * w
    convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
    p = convertToQtFormat.scaled(640, 512, Qt.KeepAspectRatio)
    return p

class ConnectDeviceThread(QThread):
    resultReady = Signal(str)
    deviceConnected = Signal(QThread)
    is_connected = False


class ConnectRobotThread(ConnectDeviceThread):
    def run(self):
        if not self.is_connected:
            print('run RobotThread')
            device = bolt_sorter_machine.connect_arduino()
            if device:
                self.deviceConnected.emit(self)
                # todo: remove signal from connect
                self.resultReady.emit("Robot connected")
                self.is_connected=True
            else:
                self.resultReady.emit("Robot couldn't find")


class ConnectArduinoThread(ConnectDeviceThread):
    def run(self):
        if not self.is_connected:
            print('run ArduinoThread')
            device = bolt_sorter_machine.connect_arduino()
            if device:
                self.deviceConnected.emit(self)
                # todo: remove signal from connect
                self.resultReady.emit("Arduino connected")
                self.is_connected=True
            else:
                self.resultReady.emit("Arduino couldn't find")


class ConnectCameraThread(ConnectDeviceThread):
    def run(self):
        if not self.is_connected:
            print('run CameraThread')
            device = bolt_sorter_machine.connect_arduino()
            if device:
                self.deviceConnected.emit(self)
                # todo: remove signal from connect
                self.resultReady.emit("Camera connected")
                self.is_connected=True
            else:
                self.resultReady.emit("Camera couldn't find")

class MainWindow(QMainWindow):
    @Slot(QImage)
    def setImage(self, image):
        self.ui.label_img_camera.setPixmap(QPixmap.fromImage(image))

    @Slot(np.ndarray)
    def setBoltFrame(self, frame): # np array
        self.ui.label_img_bolt.setPixmap(QPixmap.fromImage(frame))
        print('received at slot')

    def updateBoltCounts(self, counts):
        print('update_bolt_counts: ',counts)
        table = self.ui.tableWidget_2
        for i in range(0,table.rowCount()):
            item = QTableWidgetItem(str(counts[i]))
            item = table.setItem(i,1,item)

    def updateProgress(self, counts):
        progress = (self.sum_column_table(1)/self.bolts_total)*100
        print(progress)
        self.ui.progressBar.setValue(progress)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.next_button.setEnabled(False)
        # self.ui.next_button.clicked.connect(self.goToNext)
        self.ui.next_button.clicked.connect(self.goToNext)
        self.ui.prev_button.setEnabled(False)
        self.ui.prev_button.clicked.connect(self.goToPrev)

        self.page_index = {
            "page_system_check": self.ui.stackedWidget.indexOf(self.ui.page_system_check),
            "page_connect": self.ui.stackedWidget.indexOf(self.ui.page_connect),
            "page_select_subassembly": self.ui.stackedWidget.indexOf(self.ui.page_select_subassembly),
            "page_subassembly_overview": self.ui.stackedWidget.indexOf(self.ui.page_subassembly_overview),
            "page_machine": self.ui.stackedWidget.indexOf(self.ui.page_machine)
        }
        print(self.page_index)

        # set connect as first page
        self.ui.stackedWidget.setCurrentIndex(self.page_index['page_machine'])

        self.setupConnect()

        self.connected_devices = 0

        # add signal to connect arduino
        th = CameraThread(self)
        th.changePixmap.connect(self.setImage)
        th.start()

        self.machineThread = MachineThread()
        self.setupMachine()


    def setupMachine(self):
        self.bolts_total = self.sum_column_table(2)
        print(self.bolts_total)

        self.ui.stop_machine_button.setDisabled(True)

        # add thread to run button
        self.ui.start_machine_button.clicked.connect(self.machineThread.start)
        self.ui.start_machine_button.clicked.connect(lambda: self.ui.stop_machine_button.setEnabled(True))
        self.machineThread.started.connect(lambda: self.ui.start_machine_button.setDisabled(True))
        self.machineThread.started.connect(lambda: self.ui.start_machine_button.setText("running..."))
        # self.machineThread.finished.connect(lambda: self.ui.start_machine_button.setEnabled(True))
        self.machineThread.finished.connect(self.machineThread.start) # repeat thread

        self.ui.stop_machine_button.clicked.connect(self.machineThread.stop_machine)
        self.ui.stop_machine_button.clicked.connect(lambda: self.machineThread.disconnect(self.machineThread))
        self.ui.stop_machine_button.clicked.connect(lambda: self.ui.stop_machine_button.setText("stopping ..."))
        self.ui.stop_machine_button.clicked.connect(lambda: self.machineThread.finished.connect(self.machineDone))


        self.machineThread.BoltFrame.connect(self.setBoltFrame)
        self.machineThread.BoltType.connect(lambda x: self.ui.detected_bolt_type.setText(x))
        self.machineThread.BoltCounts.connect(self.updateBoltCounts)
        self.machineThread.BoltCounts.connect(self.updateProgress)

    def machineDone(self):
        self.ui.stop_machine_button.setDisabled(True)
        self.ui.stop_machine_button.setText("stopped")
        self.ui.start_machine_button.setText("sorted subassembly")
        self.ui.next_button.setText("Measure new subassembly >>")
        self.ui.next_button.setEnabled(True)

    def sum_column_table(self, column_no):
        # count sum of total on x bus
        table = self.ui.tableWidget_2
        sum = 0
        for i in range(0,table.rowCount()):
            item:QTableWidgetItem= table.item(i,column_no)
            sum+=int(item.text())
        return sum


    def setupConnect(self):
        self.connectRobotThread = ConnectRobotThread()
        self.connectRobotThread.resultReady.connect(lambda x: self.ui.status_robot.setText(x))
        self.connectRobotThread.finished.connect(self.connect_finished)

        self.connectArduinoThread = ConnectArduinoThread()
        self.connectArduinoThread.resultReady.connect(lambda x: self.ui.status_arduino.setText(x))
        self.connectArduinoThread.finished.connect(self.connect_finished)


        self.connectCameraThread = ConnectCameraThread()
        self.connectCameraThread.resultReady.connect(lambda x: self.ui.status_camera.setText(x))
        self.connectCameraThread.finished.connect(self.connect_finished)

        self.ui.button_connect.clicked.connect(self.connectRobotThread.start)
        self.ui.button_connect.clicked.connect(self.connectArduinoThread.start)
        self.ui.button_connect.clicked.connect(self.connectCameraThread.start)
        self.ui.button_connect.clicked.connect(lambda: self.ui.button_connect.setDisabled(True))


    def connect_finished(self):
        print("finished")
        if self.connectRobotThread.isFinished()\
                and self.connectArduinoThread.isFinished()\
                and self.connectCameraThread.isFinished(): # all are finished
            print('finished')
            self.ui.button_connect.setEnabled(True)
            if self.connectRobotThread.is_connected\
                    and self.connectArduinoThread.is_connected\
                    and self.connectCameraThread.is_connected: # check here if all devices are connected
                # delete threads
                self.connectRobotThread.deleteLater()
                self.connectArduinoThread.deleteLater()
                self.connectCameraThread.deleteLater()

                self.ui.button_connect.setDisabled(True)
                self.ui.button_connect.setText("All devices connected")
                self.ui.next_button.setEnabled(True)


    def goToNext(self):
        index = self.ui.stackedWidget.currentIndex()
        new_index = index + 1
        if(index == self.page_index['page_machine']):
            new_index = self.page_index['page_system_check']
        self.ui.stackedWidget.setCurrentIndex(new_index)

    def goToPrev(self):
        index = self.ui.stackedWidget.currentIndex()
        self.ui.stackedWidget.setCurrentIndex(index - 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
