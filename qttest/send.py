# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(QtWidgets.QMainWindow):
    clicked = pyqtSignal(list)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 376)
        MainWindow.setMinimumSize(QtCore.QSize(749, 376))
        MainWindow.setMaximumSize(QtCore.QSize(749, 376))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 741, 321))
        self.label.setMinimumSize(QtCore.QSize(741, 321))
        self.label.setMaximumSize(QtCore.QSize(741, 321))
        self.label.setStyleSheet("background-image: url(:/newPrefix/470727991b1515c36d170b0fb6d5a5e5.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 191, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 40, 72, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 40, 221, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 80, 641, 171))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 280, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "收件人"))
        self.label_3.setText(_translate("MainWindow", "标题"))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.slot_ok)
        self.pushButton_2.clicked.connect(self.slot_cancel)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setText('个人信息')

    def slot_ok(self):
        res = []
        if self.lineEdit.text() != '':
            res.append(self.lineEdit.text())
            res.append(self.lineEdit_2.text())
            res.append(self.textEdit.toPlainText())
            self.clicked.emit(res)
            self.close()
            QMessageBox.warning(self, "提醒", '发送成功', QMessageBox.Yes | QMessageBox.No)
        else:
            QMessageBox.warning(self, "提醒", '收件人不能为空', QMessageBox.Yes | QMessageBox.No)

    def slot_cancel(self):
        self.close()
import b_rc
