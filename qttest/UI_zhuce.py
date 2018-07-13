# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_zhuce.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys

import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit

import send_mail
import _thread
from 生成验证码 import Random
class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(353, 177)
        MainWindow.setMaximumSize(353, 177)
        MainWindow.setMinimumSize(353, 177)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 72, 15))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(102, 20, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(102, 60, 151, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(102, 100, 151, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 72, 15))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 30, 71, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 80, 71, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 353, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.cancel)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "注册"))
        self.label.setText(_translate("MainWindow", "注册邮箱"))
        self.label_2.setText(_translate("MainWindow", "用户名"))
        self.label_3.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "ok"))
        self.pushButton_2.setText(_translate("MainWindow", "cancel"))

    def accept(self):
        if self.lineEdit.text().__len__() != 0 and self.lineEdit_2.text().__len__() != 0 and self.lineEdit_3.text().__len__() != 0:
            if self.user_exit() == False:
                self.email = send_mail.Mail(self.lineEdit.text())
                self.ans = Random().Random(4)
                _thread.start_new_thread(self.email.send_text, (self.ans,))
                self.check()
                self.hide()
            else:
                QMessageBox.warning(self, "提醒", '用户已经存在', QMessageBox.Yes | QMessageBox.No)
        else:
            ans = ""
            if self.lineEdit.text().__len__() == 0:
                ans += '邮箱未填\n'
            if self.lineEdit_2.text().__len__() == 0:
                ans += '用户名未填\n'
            if self.lineEdit_3.text().__len__() == 0:
                ans += '密码未填或不规范\n'
            QMessageBox.warning(self, "提醒", ans, QMessageBox.Yes | QMessageBox.No)

    def cancel(self):
        self.hide()

    def check(self):
        text, ok = QInputDialog.getText(self, '输入验证码', '请输入验证码', QLineEdit.Normal, '')
        if ok == True:
            if text != self.ans:
                QMessageBox.warning(self, "提醒", '验证码错误', QMessageBox.Yes | QMessageBox.No)
            else:
                db = pymysql.connect('localhost', 'root', '123456', 'user', port=3307)
                cursor = db.cursor()
                sql = "insert into user.user_information(name, passwd, email, power) VALUE ('%s', '%s', '%s', '0')" % (self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit.text())
                print(sql)
                try:
                    cursor.execute(sql)
                    db.commit()
                    print('insert success')
                except:
                    db.rollback()
                    print('insert fail')
                db.close()

    def user_exit(self):
        db = pymysql.connect('localhost', 'root', '123456', 'user', port=3307)
        cursor = db.cursor()
        sql = "select * from user.user_information where name = '%s'" % (self.lineEdit_2.text())
        cursor.execute(sql)
        results = cursor.fetchall().__len__()
        db.close()
        return results != 0

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)