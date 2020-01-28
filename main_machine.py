from ui_main_window import Ui_MainWindow
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys, time
import machine_controller_test as machine_controller
controller = machine_controller.MachineController()

from cv2 import cv2
import ueye_camera
class Thread(QThread):
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

class ConnectDeviceThread(QThread):
    resultReady = Signal(str)
    deviceConnected = Signal(QThread)
    is_connected = False


class ConnectRobotThread(ConnectDeviceThread):
    def run(self):
        if not self.is_connected:
            print('run RobotThread')
            device = controller.connect_arduino()
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
            device = controller.connect_arduino()
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
            device = controller.connect_arduino()
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
        self.ui.label_img_bolt.setPixmap(QPixmap.fromImage(image))

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.next_button.setEnabled(False)
        # self.ui.next_button.clicked.connect(self.goToNext)
        self.ui.next_button.clicked.connect(self.goToNext)
        self.ui.prev_button.setEnabled(False)
        self.ui.prev_button.clicked.connect(self.goToPrev)

        page_index = {
            "page_system_check": self.ui.stackedWidget.indexOf(self.ui.page_system_check),
            "page_connect": self.ui.stackedWidget.indexOf(self.ui.page_connect),
            "page_select_subassembly": self.ui.stackedWidget.indexOf(self.ui.page_select_subassembly),
            "page_subassembly_overview": self.ui.stackedWidget.indexOf(self.ui.page_subassembly_overview),
            "page_machine": self.ui.stackedWidget.indexOf(self.ui.page_machine)
        }
        print(page_index)

        # set connect as first page
        self.ui.stackedWidget.setCurrentIndex(page_index['page_machine'])

        self.setupConnect()

        self.connected_devices = 0

        # add signal to connect arduino
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()

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
        self.ui.stackedWidget.setCurrentIndex(index + 1)

    def goToPrev(self):
        index = self.ui.stackedWidget.currentIndex()
        self.ui.stackedWidget.setCurrentIndex(index - 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
