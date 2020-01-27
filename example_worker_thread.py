import sys
from PySide2.QtCore import QObject, Slot, Signal, QThread
from ui_main_window import Ui_MainWindow
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys

# Create the Slots that will receive signals
@Slot(str)
def update_a_str_field(message):
    print(message)

@Slot(int)
def update_a_int_field(self, value):
    print(value)

# Signals must inherit QObject
class Communicate(QObject):
    signal_str = Signal(str)
    signal_int = Signal(int)

class WorkerThread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.signals = Communicate()
        # Connect the signals to the main thread slots
        self.signals.signal_str.connect(parent.update_a_str_field)
        self.signals.signal_int.connect(parent.update_a_int_field)

    def run(self):
        self.signals.update_a_int_field.emit(1)
        self.signals.update_a_str_field.emit("Hello World.")

class Worker(QObject):
    resultReady = Signal(str)

    @Slot(str)
    def doWork(self, parameter):
        self.resultReady.emit(str('worker'))


class Controller(QObject):
    operate = Signal(str)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.workerThread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.workerThread)
        self.worker.finished.connect(self.worker.deleteLater)
        self.operate.connect(self.worker.doWork)
        self.worker.resultReady.connect(self.handleResults)

    def __del__(self):
        self.workerThread.quit()
        self.workerThread.wait()

    @Slot(str)
    def handleResults(self, val):
        print(val)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Controller()
    window.start()

    sys.exit(app.exec_())
# Erroneous: refers to class Communicate, not an instance of the class
# Communicate.speak.connect(say_something)
# raises exception: AttributeError: 'PySide2.QtCore.Signal' object has no attribute 'connect'