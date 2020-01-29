# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1102, 1041)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.prev_button = QPushButton(self.centralwidget)
        self.prev_button.setObjectName(u"prev_button")
        self.prev_button.setEnabled(False)

        self.gridLayout.addWidget(self.prev_button, 1, 0, 1, 1)

        self.next_button = QPushButton(self.centralwidget)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setEnabled(False)

        self.gridLayout.addWidget(self.next_button, 1, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_connect = QWidget()
        self.page_connect.setObjectName(u"page_connect")
        self.verticalLayout_2 = QVBoxLayout(self.page_connect)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_2 = QLabel(self.page_connect)
        self.title_2.setObjectName(u"title_2")

        self.verticalLayout_2.addWidget(self.title_2)

        self.status_robot = QLabel(self.page_connect)
        self.status_robot.setObjectName(u"status_robot")

        self.verticalLayout_2.addWidget(self.status_robot)

        self.status_arduino = QLabel(self.page_connect)
        self.status_arduino.setObjectName(u"status_arduino")

        self.verticalLayout_2.addWidget(self.status_arduino)

        self.status_camera = QLabel(self.page_connect)
        self.status_camera.setObjectName(u"status_camera")

        self.verticalLayout_2.addWidget(self.status_camera)

        self.button_connect = QPushButton(self.page_connect)
        self.button_connect.setObjectName(u"button_connect")

        self.verticalLayout_2.addWidget(self.button_connect)

        self.stackedWidget.addWidget(self.page_connect)
        self.page_system_check = QWidget()
        self.page_system_check.setObjectName(u"page_system_check")
        self.verticalLayout = QVBoxLayout(self.page_system_check)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.page_system_check)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.title)

        self.checkBox = QCheckBox(self.page_system_check)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.page_system_check)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.confirm_button = QPushButton(self.page_system_check)
        self.confirm_button.setObjectName(u"confirm_button")

        self.verticalLayout.addWidget(self.confirm_button)

        self.stackedWidget.addWidget(self.page_system_check)
        self.page_select_subassembly = QWidget()
        self.page_select_subassembly.setObjectName(u"page_select_subassembly")
        self.gridLayout_2 = QGridLayout(self.page_select_subassembly)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.search_box = QLineEdit(self.page_select_subassembly)
        self.search_box.setObjectName(u"search_box")

        self.gridLayout_2.addWidget(self.search_box, 1, 1, 1, 1)

        self.treeWidget = QTreeWidget(self.page_select_subassembly)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setAnimated(True)

        self.gridLayout_2.addWidget(self.treeWidget, 2, 0, 1, 2)

        self.selected_title = QLabel(self.page_select_subassembly)
        self.selected_title.setObjectName(u"selected_title")

        self.gridLayout_2.addWidget(self.selected_title, 3, 0, 1, 1)

        self.selected_status = QLabel(self.page_select_subassembly)
        self.selected_status.setObjectName(u"selected_status")

        self.gridLayout_2.addWidget(self.selected_status, 3, 1, 1, 1)

        self.title_3 = QLabel(self.page_select_subassembly)
        self.title_3.setObjectName(u"title_3")

        self.gridLayout_2.addWidget(self.title_3, 0, 0, 1, 2)

        self.search_title = QLabel(self.page_select_subassembly)
        self.search_title.setObjectName(u"search_title")

        self.gridLayout_2.addWidget(self.search_title, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_select_subassembly)
        self.page_subassembly_overview = QWidget()
        self.page_subassembly_overview.setObjectName(u"page_subassembly_overview")
        self.gridLayout_3 = QGridLayout(self.page_subassembly_overview)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.selected_title_2 = QLabel(self.page_subassembly_overview)
        self.selected_title_2.setObjectName(u"selected_title_2")

        self.gridLayout_3.addWidget(self.selected_title_2, 1, 0, 1, 1)

        self.selected_status_2 = QLabel(self.page_subassembly_overview)
        self.selected_status_2.setObjectName(u"selected_status_2")

        self.gridLayout_3.addWidget(self.selected_status_2, 1, 1, 1, 1)

        self.tableWidget = QTableWidget(self.page_subassembly_overview)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(5, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(5, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(6, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(6, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(7, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(7, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(8, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setItem(8, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setItem(9, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setItem(9, 1, __qtablewidgetitem31)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.tableWidget, 2, 0, 1, 3)

        self.title_4 = QLabel(self.page_subassembly_overview)
        self.title_4.setObjectName(u"title_4")

        self.gridLayout_3.addWidget(self.title_4, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.page_subassembly_overview)
        self.page_machine = QWidget()
        self.page_machine.setObjectName(u"page_machine")
        self.horizontalLayout = QHBoxLayout(self.page_machine)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.selected_title_3 = QLabel(self.page_machine)
        self.selected_title_3.setObjectName(u"selected_title_3")

        self.gridLayout_4.addWidget(self.selected_title_3, 3, 0, 1, 1)

        self.progressBar = QProgressBar(self.page_machine)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_4.addWidget(self.progressBar, 5, 0, 1, 2)

        self.selected_status_3 = QLabel(self.page_machine)
        self.selected_status_3.setObjectName(u"selected_status_3")

        self.gridLayout_4.addWidget(self.selected_status_3, 3, 1, 1, 1)

        self.tableWidget_2 = QTableWidget(self.page_machine)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        if (self.tableWidget_2.rowCount() < 10):
            self.tableWidget_2.setRowCount(10)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 2, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 2, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_2.setItem(6, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_2.setItem(6, 2, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_2.setItem(7, 0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_2.setItem(7, 2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_2.setItem(8, 0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_2.setItem(8, 2, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_2.setItem(9, 0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_2.setItem(9, 2, __qtablewidgetitem64)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.gridLayout_4.addWidget(self.tableWidget_2, 6, 0, 1, 2)

        self.start_machine_button = QPushButton(self.page_machine)
        self.start_machine_button.setObjectName(u"start_machine_button")

        self.gridLayout_4.addWidget(self.start_machine_button, 0, 0, 1, 1)

        self.stop_machine_button = QPushButton(self.page_machine)
        self.stop_machine_button.setObjectName(u"stop_machine_button")

        self.gridLayout_4.addWidget(self.stop_machine_button, 0, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_4)

        self.line_2 = QFrame(self.page_machine)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_img_camera = QLabel(self.page_machine)
        self.label_img_camera.setObjectName(u"label_img_camera")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_img_camera.sizePolicy().hasHeightForWidth())
        self.label_img_camera.setSizePolicy(sizePolicy)
        self.label_img_camera.setMinimumSize(QSize(480, 384))
        self.label_img_camera.setFrameShape(QFrame.Box)

        self.verticalLayout_3.addWidget(self.label_img_camera)

        self.line = QFrame(self.page_machine)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label_img_bolt = QLabel(self.page_machine)
        self.label_img_bolt.setObjectName(u"label_img_bolt")
        sizePolicy.setHeightForWidth(self.label_img_bolt.sizePolicy().hasHeightForWidth())
        self.label_img_bolt.setSizePolicy(sizePolicy)
        self.label_img_bolt.setMinimumSize(QSize(480, 384))
        self.label_img_bolt.setFrameShape(QFrame.Box)

        self.verticalLayout_3.addWidget(self.label_img_bolt)

        self.detected_bolt_type = QLabel(self.page_machine)
        self.detected_bolt_type.setObjectName(u"detected_bolt_type")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.detected_bolt_type.sizePolicy().hasHeightForWidth())
        self.detected_bolt_type.setSizePolicy(sizePolicy1)
        self.detected_bolt_type.setMinimumSize(QSize(320, 0))

        self.verticalLayout_3.addWidget(self.detected_bolt_type)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.stackedWidget.addWidget(self.page_machine)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1102, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.prev_button.setText(QCoreApplication.translate("MainWindow", u"Previous <<", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"Next >>", None))
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"Connect to devices", None))
        self.status_robot.setText(QCoreApplication.translate("MainWindow", u"robot unconnnected", None))
        self.status_arduino.setText(QCoreApplication.translate("MainWindow", u"arduino unconnected", None))
        self.status_camera.setText(QCoreApplication.translate("MainWindow", u"camera unconnected", None))
        self.button_connect.setText(QCoreApplication.translate("MainWindow", u"connect everything", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"System Check", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"The machine is empty", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"The bins are empty", None))
        self.confirm_button.setText(QCoreApplication.translate("MainWindow", u"confirm", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"No. of items", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"No. of types", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Subassemblies", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"297", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"?", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Engine", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"100", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"?", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"X-1", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"100", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"?", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"X-50", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("MainWindow", u"97", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"10", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"X-99", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.selected_title.setText(QCoreApplication.translate("MainWindow", u"Selected engine/subassembly:", None))
        self.selected_status.setText(QCoreApplication.translate("MainWindow", u"engine/subassembly", None))
        self.title_3.setText(QCoreApplication.translate("MainWindow", u"Select subassembly", None))
        self.search_title.setText(QCoreApplication.translate("MainWindow", u"Search:", None))
        self.selected_title_2.setText(QCoreApplication.translate("MainWindow", u"Selected engine/subassembly", None))
        self.selected_status_2.setText(QCoreApplication.translate("MainWindow", u"XEN/X99", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"bolt type", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"amount in subassembly", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"10", None));

        __sortingEnabled1 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem12 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"V647P23B", None));
        ___qtablewidgetitem13 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"M59557-10", None));
        ___qtablewidgetitem15 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem16 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"M59557-16", None));
        ___qtablewidgetitem17 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem18 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"M59557-20", None));
        ___qtablewidgetitem19 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem20 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"NAS1802-3-6", None));
        ___qtablewidgetitem21 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem22 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"NAS1802-3-7", None));
        ___qtablewidgetitem23 = self.tableWidget.item(5, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem24 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"NAS1802-3-8", None));
        ___qtablewidgetitem25 = self.tableWidget.item(6, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem26 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"NAS1802-3-9", None));
        ___qtablewidgetitem27 = self.tableWidget.item(7, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem28 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"NAS1802-4-07", None));
        ___qtablewidgetitem29 = self.tableWidget.item(8, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem30 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"NAS6305-10", None));
        ___qtablewidgetitem31 = self.tableWidget.item(9, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"10", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled1)

        self.title_4.setText(QCoreApplication.translate("MainWindow", u"Subassembly overview", None))
        self.selected_title_3.setText(QCoreApplication.translate("MainWindow", u"selected engine/subassembly:", None))
        self.selected_status_3.setText(QCoreApplication.translate("MainWindow", u"XEN/X99", None))
        ___qtablewidgetitem32 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"bolt type", None));
        ___qtablewidgetitem33 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"count", None));
        ___qtablewidgetitem34 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"expected count", None));
        ___qtablewidgetitem35 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem36 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem37 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem38 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem39 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem40 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem41 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem42 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem43 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem44 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"10", None));

        __sortingEnabled2 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem45 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"V647P23B", None));
        ___qtablewidgetitem46 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem47 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"M59557-10", None));
        ___qtablewidgetitem48 = self.tableWidget_2.item(1, 2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem49 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"M59557-16", None));
        ___qtablewidgetitem50 = self.tableWidget_2.item(2, 2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem51 = self.tableWidget_2.item(3, 0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"M59557-20", None));
        ___qtablewidgetitem52 = self.tableWidget_2.item(3, 2)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem53 = self.tableWidget_2.item(4, 0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"NAS1802-3-6", None));
        ___qtablewidgetitem54 = self.tableWidget_2.item(4, 2)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem55 = self.tableWidget_2.item(5, 0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"NAS1802-3-7", None));
        ___qtablewidgetitem56 = self.tableWidget_2.item(5, 2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem57 = self.tableWidget_2.item(6, 0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"NAS1802-3-8", None));
        ___qtablewidgetitem58 = self.tableWidget_2.item(6, 2)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem59 = self.tableWidget_2.item(7, 0)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"NAS1802-3-9", None));
        ___qtablewidgetitem60 = self.tableWidget_2.item(7, 2)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem61 = self.tableWidget_2.item(8, 0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"NAS1802-4-07", None));
        ___qtablewidgetitem62 = self.tableWidget_2.item(8, 2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem63 = self.tableWidget_2.item(9, 0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"NAS6305-10", None));
        ___qtablewidgetitem64 = self.tableWidget_2.item(9, 2)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"10", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled2)

        self.start_machine_button.setText(QCoreApplication.translate("MainWindow", u"start sorting machine", None))
        self.stop_machine_button.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.label_img_camera.setText(QCoreApplication.translate("MainWindow", u"Live camera feed", None))
        self.label_img_bolt.setText(QCoreApplication.translate("MainWindow", u"Detected bolt image", None))
        self.detected_bolt_type.setText(QCoreApplication.translate("MainWindow", u"Detected bolt", None))
    # retranslateUi

