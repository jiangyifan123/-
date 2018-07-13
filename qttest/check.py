# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check.ui'
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
        MainWindow.resize(878, 514)
        MainWindow.setStyleSheet("")
        self.setMinimumSize(878, 514)
        self.setMaximumSize(878, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(520, 360, 181, 21))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 390, 481, 21))
        self.lineEdit_3.setMinimumSize(QtCore.QSize(481, 21))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(481, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(520, 240, 181, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(160, 40, 461, 151))
        self.listWidget.setObjectName("listWidget")
        self.label_56 = QtWidgets.QLabel(self.centralwidget)
        self.label_56.setGeometry(QtCore.QRect(160, 320, 31, 15))
        self.label_56.setMinimumSize(QtCore.QSize(31, 15))
        self.label_56.setMaximumSize(QtCore.QSize(31, 15))
        self.label_56.setObjectName("label_56")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 200, 181, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(630, 160, 93, 28))
        self.pushButton_17.setMinimumSize(QtCore.QSize(93, 28))
        self.pushButton_17.setMaximumSize(QtCore.QSize(93, 28))
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
        self.label_49.setGeometry(QtCore.QRect(440, 320, 72, 15))
        self.label_49.setMinimumSize(QtCore.QSize(72, 15))
        self.label_49.setMaximumSize(QtCore.QSize(72, 15))
        self.label_49.setObjectName("label_49")
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        self.label_48.setGeometry(QtCore.QRect(160, 360, 31, 15))
        self.label_48.setMinimumSize(QtCore.QSize(31, 15))
        self.label_48.setMaximumSize(QtCore.QSize(31, 15))
        self.label_48.setObjectName("label_48")
        self.label_52 = QtWidgets.QLabel(self.centralwidget)
        self.label_52.setGeometry(QtCore.QRect(440, 280, 72, 15))
        self.label_52.setMinimumSize(QtCore.QSize(72, 15))
        self.label_52.setMaximumSize(QtCore.QSize(72, 15))
        self.label_52.setObjectName("label_52")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(630, 120, 93, 28))
        self.pushButton_18.setMinimumSize(QtCore.QSize(93, 28))
        self.pushButton_18.setMaximumSize(QtCore.QSize(93, 28))
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_55 = QtWidgets.QLabel(self.centralwidget)
        self.label_55.setGeometry(QtCore.QRect(440, 240, 72, 15))
        self.label_55.setMinimumSize(QtCore.QSize(72, 15))
        self.label_55.setMaximumSize(QtCore.QSize(72, 15))
        self.label_55.setObjectName("label_55")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(230, 360, 181, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_53 = QtWidgets.QLabel(self.centralwidget)
        self.label_53.setGeometry(QtCore.QRect(160, 240, 31, 15))
        self.label_53.setMinimumSize(QtCore.QSize(31, 15))
        self.label_53.setMaximumSize(QtCore.QSize(31, 15))
        self.label_53.setObjectName("label_53")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(520, 320, 181, 21))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setGeometry(QtCore.QRect(160, 200, 31, 15))
        self.label_50.setMinimumSize(QtCore.QSize(31, 15))
        self.label_50.setMaximumSize(QtCore.QSize(31, 15))
        self.label_50.setObjectName("label_50")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 240, 181, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setGeometry(QtCore.QRect(131, 390, 61, 20))
        self.label_47.setMinimumSize(QtCore.QSize(61, 20))
        self.label_47.setMaximumSize(QtCore.QSize(61, 20))
        self.label_47.setObjectName("label_47")
        self.label_54 = QtWidgets.QLabel(self.centralwidget)
        self.label_54.setGeometry(QtCore.QRect(160, 280, 31, 15))
        self.label_54.setMinimumSize(QtCore.QSize(31, 15))
        self.label_54.setMaximumSize(QtCore.QSize(31, 15))
        self.label_54.setObjectName("label_54")
        self.label_51 = QtWidgets.QLabel(self.centralwidget)
        self.label_51.setGeometry(QtCore.QRect(440, 360, 72, 15))
        self.label_51.setMinimumSize(QtCore.QSize(72, 15))
        self.label_51.setMaximumSize(QtCore.QSize(72, 15))
        self.label_51.setObjectName("label_51")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(230, 320, 181, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(520, 280, 181, 21))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 280, 181, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 841, 441))
        self.label.setStyleSheet("background-image: url(:/newPrefix/470727991b1515c36d170b0fb6d5a5e5.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(520, 200, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 200, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.lineEdit_12.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_9.raise_()
        self.listWidget.raise_()
        self.label_56.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_17.raise_()
        self.label_49.raise_()
        self.label_48.raise_()
        self.label_52.raise_()
        self.pushButton_18.raise_()
        self.label_55.raise_()
        self.lineEdit_8.raise_()
        self.label_53.raise_()
        self.lineEdit_11.raise_()
        self.label_50.raise_()
        self.lineEdit_4.raise_()
        self.label_47.raise_()
        self.label_54.raise_()
        self.label_51.raise_()
        self.lineEdit_7.raise_()
        self.lineEdit_10.raise_()
        self.lineEdit_6.raise_()
        self.comboBox.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 878, 26))
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
        self.lineEdit_3.setText(_translate("MainWindow", "单独给出会根据所给的信息含有的关键字查询相关房源"))
        self.label_56.setText(_translate("MainWindow", "楼层"))
        self.pushButton_17.setText(_translate("MainWindow", "取消"))
        self.label_49.setText(_translate("MainWindow", "房型"))
        self.label_48.setText(_translate("MainWindow", "装修"))
        self.label_52.setText(_translate("MainWindow", "建造年代"))
        self.pushButton_18.setText(_translate("MainWindow", "确认"))
        self.label_55.setText(_translate("MainWindow", "房屋类型"))
        self.label_53.setText(_translate("MainWindow", "售价"))
        self.label_50.setText(_translate("MainWindow", "区域"))
        self.label_47.setText(_translate("MainWindow", "详细地址"))
        self.label_54.setText(_translate("MainWindow", "面积"))
        self.label_51.setText(_translate("MainWindow", "朝向"))
        self.comboBox.setItemText(0, _translate("MainWindow", "综合排序"))
        self.comboBox.setItemText(1, _translate("MainWindow", "售价"))
        self.comboBox.setItemText(2, _translate("MainWindow", "区域"))
        self.comboBox.setItemText(3, _translate("MainWindow", "房屋类型"))
        self.comboBox.setItemText(4, _translate("MainWindow", "面积"))
        self.label_2.setText(_translate("MainWindow", "排序方式"))

    def __init__(self, item, lib, name = None):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.item = item
        self.tmplib = lib
        self.lib = []
        self.dic = {}
        self.name = name
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_11.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_12.setEnabled(False)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.setup()
        self.display()
        self.listWidget.itemClicked.connect(self.slot_display)
        self.pushButton_17.clicked.connect(self.slot_cancel)
        self.comboBox.currentIndexChanged.connect(self.slot_paixu)
        self.pushButton_18.clicked.connect(self.slot_queding)

    def setup(self):
        for i in self.tmplib:
            res = 0
            i = list(i)
            for k in range(len(self.item)):
                if i[k] == self.item[k]:
                    res += 1
            i.append(res)
            self.lib.append(i)

    def display(self):
        self.lib.sort(key= lambda lib: lib[10], reverse=True)
        counts = 0
        self.dic.clear()
        for i in self.lib:
            s = '选项' + str(counts)
            self.dic[s] = i
            self.listWidget.addItem(s)
            counts += 1

    def slot_display(self, item):
        res = self.dic[item.text()]
        self.lineEdit_5.setText(res[0])
        self.lineEdit_9.setText(res[1])
        self.lineEdit_4.setText(res[2])
        self.lineEdit_10.setText(res[3])
        self.lineEdit_6.setText(res[4])
        self.lineEdit_11.setText(res[5])
        self.lineEdit_7.setText(res[6])
        self.lineEdit_12.setText(res[7])
        self.lineEdit_8.setText(res[8])
        self.lineEdit_3.setText(res[9])

    def slot_cancel(self):
        self.close()

    def slot_paixu(self, index):
        s = self.comboBox.itemText(index)
        self.listWidget.clear()
        if s == '综合排序':
            self.lib.sort(key= lambda lib: lib[10], reverse=True)
        elif s == '售价':
            self.lib.sort(key= lambda lib: 20 if lib[2] == self.item[2] else lib[10], reverse=True)
        elif s == '区域':
            self.lib.sort(key=lambda lib: 20 if lib[0] == self.item[0] else lib[10], reverse=True)
        elif s == '房屋类型':
            self.lib.sort(key=lambda lib: 20 if lib[1] == self.item[1] else lib[10], reverse=True)
        elif s == '面积':
            self.lib.sort(key=lambda lib: 20 if lib[4] == self.item[4] else lib[10], reverse=True)
        counts = 0
        self.dic.clear()
        for i in self.lib:
            s = '选项' + str(counts)
            self.dic[s] = i
            self.listWidget.addItem(s)
            counts += 1

    def set_user_name(self, user_name, num, num1):
        self.user_name = user_name
        self.num = num
        self.num1 = num1

    def slot_queding(self):
        reply = QMessageBox.question(self, "提醒", '确认吗？', QMessageBox.Yes | QMessageBox.No)
        if self.name == '订单' and reply == QMessageBox.Yes:
            d = self.listWidget.currentRow()
            if d != -1:
                item = self.listWidget.item(d)
                res = self.dic[item.text()]
                t = res + [self.user_name, self.num, self.num1]
                self.clicked.emit(t)
import b_rc