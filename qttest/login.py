# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
import sys
from tkinter import PhotoImage

import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from PyQt5.QtCore import *

import MainForm
import UI_zhuce
import change_passwd
import config


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 403)
        MainWindow.setMaximumSize(523, 403)
        MainWindow.setMinimumSize(523, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginbtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginbtn.setGeometry(QtCore.QRect(150, 300, 231, 41))
        self.loginbtn.setObjectName("loginbtn")
        self.account_text = QtWidgets.QLineEdit(self.centralwidget)
        self.account_text.setGeometry(QtCore.QRect(150, 210, 231, 31))
        self.account_text.setText("")
        self.account_text.setObjectName("account_text")
        self.account_text.textChanged.connect(self.shot_text_change)
        self.passwd_text = QtWidgets.QLineEdit(self.centralwidget)
        self.passwd_text.setGeometry(QtCore.QRect(150, 240, 231, 31))
        self.passwd_text.setObjectName("passwd_text")
        self.passwd_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.remember_passwd = QtWidgets.QCheckBox(self.centralwidget)
        self.remember_passwd.setGeometry(QtCore.QRect(150, 280, 91, 19))
        self.remember_passwd.setObjectName("remember_passwd")
        self.autologin = QtWidgets.QCheckBox(self.centralwidget)
        self.autologin.setGeometry(QtCore.QRect(290, 280, 91, 19))
        self.autologin.setObjectName("autologin")
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setGeometry(QtCore.QRect(390, 210, 71, 28))
        self.register_2.setObjectName("register_2")
        self.find_passwd = QtWidgets.QPushButton(self.centralwidget)
        self.find_passwd.setGeometry(QtCore.QRect(390, 240, 71, 28))
        self.find_passwd.setObjectName("find_passwd")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 521, 191))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")

        self.GIF1 = QMovie(r'F:\qttest\GIF1.gif')
        self.label.setMovie(self.GIF1)

        self.GIF1.start()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 210, 72, 61))
        self.label_2.setStyleSheet("image: url(:/a/8694a4c27d1ed21b526a6c8cad6eddc451da3f33.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.register_2.clicked.connect(self.shot_zhuce)
        self.find_passwd.clicked.connect(self.shot_newpasswd)
        self.loginbtn.clicked.connect(self.shot_login)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登陆"))
        self.loginbtn.setText(_translate("MainWindow", "登录"))
        self.remember_passwd.setText(_translate("MainWindow", "记住密码"))
        self.autologin.setText(_translate("MainWindow", "自动登录"))
        self.register_2.setText(_translate("MainWindow", "注册账号"))
        self.find_passwd.setText(_translate("MainWindow", "找回密码"))

    def shot_zhuce(self):#注册
        print("注册")
        self.window = UI_zhuce.Ui_MainWindow()
        self.window.show()

    def shot_newpasswd(self):#找回密码
        print('改密码')
        self.window = change_passwd.Ui_MainWindow()
        self.window.show()

    def shot_login(self):#登陆键
        print('登陆')
        if self.account_text.text().__len__() != 0 and self.passwd_text.text().__len__() != 0:
            db = pymysql.connect('localhost', 'root', '123456', 'user', port=3307)
            cursor = db.cursor()
            sql = "select * from user.user_information where (name = '%s' and passwd = '%s')" % (self.account_text.text(), self.passwd_text.text())
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                if results.__len__() != 0:
                    if self.remember_passwd.isChecked() == True:
                        sql = "update user_information set last_login = '%s' where name = '%s'" % (results[0][1], self.account_text.text())
                    else:
                        sql = "update user_information set last_login = '' where name = '%s'" % (self.account_text.text())
                    user = results[0]
                    # print(user)
                    cursor.execute(sql)
                    db.commit()
                    print('login success')
                    self.window = MainForm.Ui_MainWindow()
                    Config = config.config(self.window)
                    Config.hideWindows(user[4], user[0])
                    self.window.show()
                    self.close()
                else:
                    QMessageBox.warning(self, "提醒", '用户名或者密码错误', QMessageBox.Yes | QMessageBox.No)
            except:
                print('error')
            db.close()

    def shot_text_change(self):
        try:
            db = pymysql.connect('localhost', 'root', '123456', 'user', port=3307)
            cursor = db.cursor()
            sql = "select * from user.user_information where name = '%s'" % (self.account_text.text())
            cursor.execute(sql)
            results = cursor.fetchall()
            if results.__len__() != 0 and results[0][3].__len__() != 0:
                self.passwd_text.setText(results[0][3])
                self.remember_passwd.setChecked(True)
            else:
                self.passwd_text.setText('')
                self.remember_passwd.setChecked(False)
            db.close()
        except:
            print('error datebase')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.shot_login()

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)


import a_rc