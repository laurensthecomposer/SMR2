from ui_main_window import Ui_MainWindow
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.next_button.setEnabled(True)
        self.ui.next_button.clicked.connect(self.goToNext)
        self.ui.prev_button.setEnabled(True)
        self.ui.prev_button.clicked.connect(self.goToPrev)

        page_index = {
            "page_system_check": self.ui.stackedWidget.indexOf(self.ui.page_system_check),
            "page_connect": self.ui.stackedWidget.indexOf(self.ui.page_connect),
            "page_select_subassembly": self.ui.stackedWidget.indexOf(self.ui.page_select_subassembly),
            "page_subassembly_overview": self.ui.stackedWidget.indexOf(self.ui.page_subassembly_overview),
            "page_machine": self.ui.stackedWidget.indexOf(self.ui.page_machine)
        }
        print(page_index)

        self.ui.stackedWidget.setCurrentIndex(page_index['page_connect'])

        self.setupConnect()

    def setupConnect(self):

        self.ui.button_connect.clicked.connect(self.connect)

    def connect(self):
        print('Connecting')

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