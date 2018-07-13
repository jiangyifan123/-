# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_power.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 133)
        MainWindow.setMinimumSize(QtCore.QSize(514, 133))
        MainWindow.setMaximumSize(QtCore.QSize(514, 133))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 20, 281, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 50, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 50, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 26))
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
        self.label.setText(_translate("MainWindow", "请输入用户名"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.slot_queidng)
        self.pushButton_2.clicked.connect(self.slot_cancel)

    def slot_queidng(self):
        res = QMessageBox.question(self, "提醒", '是否确认', QMessageBox.Yes | QMessageBox.No)
        if res:
            flag = False
            try:
                db = pymysql.connect('localhost', 'root', '123456', port=3307, charset='utf8')
                cursor = db.cursor()
                sql = "update user.user_information set power=1 where name= '%s'" % (self.lineEdit.text())
                cursor.execute(sql)
                db.commit()
                db.close()
                flag = True
            except:
                print('slot_queding error')
                db.rollback()
            if flag:
                self.close()

    def slot_cancel(self):
        self.close()