# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QScrollArea,
    QSizePolicy, QWidget)
import images_rc
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 570)
        self.search_lineEdit = QLineEdit(Form)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setGeometry(QRect(90, 103, 542, 41))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(17)
        self.search_lineEdit.setFont(font)
        self.search_button = QPushButton(Form)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(652, 103, 43, 43))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 170, 211, 41))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(90, 230, 611, 301))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 609, 299))
        self.listWidget = QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 611, 301))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.close_button = QPushButton(Form)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(744, 29, 30, 30))
        self.mini_button = QPushButton(Form)
        self.mini_button.setObjectName(u"mini_button")
        self.mini_button.setGeometry(QRect(700, 29, 30, 30))
        self.download_button = QPushButton(Form)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setGeometry(QRect(520, 170, 45, 45))
        self.clear_button = QPushButton(Form)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(340, 170, 45, 45))
        self.clear_label = QLabel(Form)
        self.clear_label.setObjectName(u"clear_label")
        self.clear_label.setGeometry(QRect(392, 177, 71, 31))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(15)
        self.clear_label.setFont(font2)
        self.download_label = QLabel(Form)
        self.download_label.setObjectName(u"download_label")
        self.download_label.setGeometry(QRect(574, 182, 81, 21))
        self.download_label.setFont(font2)
        self.msg_frame = QFrame(Form)
        self.msg_frame.setObjectName(u"msg_frame")
        self.msg_frame.setGeometry(QRect(280, 130, 231, 271))
        self.msg_frame.setFrameShape(QFrame.StyledPanel)
        self.msg_frame.setFrameShadow(QFrame.Raised)
        self.msg_label = QLabel(self.msg_frame)
        self.msg_label.setObjectName(u"msg_label")
        self.msg_label.setGeometry(QRect(60, 70, 111, 51))
        self.msg_label.setFont(font1)
        self.back_button = QPushButton(self.msg_frame)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(40, 180, 161, 41))
        self.back_button.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u641c\u7d22\u7ed3\u679c", None))
        self.clear_label.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.download_label.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d", None))
        self.msg_label.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u5b8c\u6210", None))
        self.back_button.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
    # retranslateUi

