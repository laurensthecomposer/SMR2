
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PySide2.QtCore import QFile, QThread, Qt
from PySide2.QtGui import QImage, QPixmap
from ui_bolts import Ui_MainWindow
from cv2 import cv2

from PySide2.QtCore import Signal, Slot
import ueye_camera
class Thread(QThread):
    changePixmap = Signal(QImage)

    def run(self):
        cap = ueye_camera.UeyeCameraCapture(1)
        while True:
            ret, frame = cap.read()
            if ret:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    @Slot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    def initUI(self):
        # self.setWindowTitle(self.title)

        # self.setGeometry(self.left, self.top, self.width, self.height)
        self.resize(1000, 1000)
        # create a label
        self.label = QLabel(self)
        self.label.move(280, 120)
        self.label.resize(640, 480)
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = App()
    window.show()

    sys.exit(app.exec_())