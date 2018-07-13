# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_passwd.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys

import _thread
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit

import send_mail
from 生成验证码 import Random


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(388, 191)
        MainWindow.setMaximumSize(388, 191)
        MainWindow.setMinimumSize(388, 191)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 91, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 221, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 100, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 388, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.ok)
        self.pushButton_2.clicked.connect(self.cancel)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "change_passwd"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.pushButton.setText(_translate("MainWindow", "ok"))
        self.pushButton_2.setText(_translate("MainWindow", "cancel"))

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def ok(self):
        db = pymysql.connect('localhost', 'root', '123456', 'user')
        cursor = db.cursor()
        sql = "select * from user.user_information where name = '%s'" % (self.lineEdit.text())
        cursor.execute(sql)
        self.results = cursor.fetchall()
        if self.results.__len__() != 0:
            Email = self.results[0][2]
            self.email = send_mail.Mail(Email)
            self.ans = Random().Random(4)
            _thread.start_new_thread(self.email.send_text, (self.ans,))
            self.check()
        else:
            QMessageBox.warning(self, "提醒", '找不到该用户', QMessageBox.Yes | QMessageBox.No)
        db.close()
        self.hide()

    def cancel(self):
        self.hide()

    def check(self):
        text, ok = QInputDialog.getText(self, '验证', '请输入验证码', QLineEdit.Normal, '')
        if ok == True:
            if text != self.ans:
                QMessageBox.warning(self, "提醒", '验证码错误', QMessageBox.Yes | QMessageBox.No)
            else:
                text1, ok1 = QInputDialog.getText(self, '验证成功', '请输入新密码', QLineEdit.Normal, '')
                if ok1 == True:
                    db = pymysql.connect('localhost', 'root', '123456', 'user')
                    cursor = db.cursor()
                    sql = "update user_information set passwd = '%s' where name = '%s'" % (text1, self.lineEdit.text())
                    try:
                        cursor.execute(sql)
                        db.commit()
                        print('update success')
                    except:
                        print('error')
                    db.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    UI = Ui_MainWindow()
    UI.show()
    sys.exit(app.exec_())
