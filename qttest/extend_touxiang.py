# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extend_touxiang.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow, add):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(944, 753)
        MainWindow.setMinimumSize(944, 753)
        MainWindow.setMaximumSize(944, 753)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 941, 701))
        self.label.setMinimumSize(QtCore.QSize(941, 701))
        self.label.setMaximumSize(QtCore.QSize(941, 701))
        self.label.setStyleSheet(add)
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 944, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "头像"))

    def __init__(self, add):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self, add)