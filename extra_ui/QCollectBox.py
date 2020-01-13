from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
import random


class QTitle( QLabel ):
    def __init__(self, parent):
        super().__init__( parent )


class QCollectBox( QFrame ):
    def __init__(self, widget):
        super().__init__( widget )

        self.setFrameStyle( QFrame.Panel | QFrame.Raised )
        self.setLineWidth( 3 )
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        self.button = QPushButton( "Click me!" )

        self.text = QLabel( "Hello World" )
        self.text.setAlignment( Qt.AlignCenter )


        self.layout = QVBoxLayout()
        self.layout.addWidget( self.text )
        self.layout.addWidget( self.button )
        self.setLayout( self.layout )
        self.button.clicked.connect( self.magic )

        self.setStyleSheet("QLabel { font-size: 40px; font-weight:bold; }")

    def setObjectName(self, name:str):
        super().setObjectName(name)
        self.text.setText("Box "+ name[4:])

    def magic(self):
        self.text.setText( random.choice( self.hello ) )
