from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QPushButton


class QQPushButton(QPushButton):
    clicked = pyqtSignal(int)
    def __init__(self, num = None, init = None):
        super(QQPushButton, self).__init__(init)
        self.num = num

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit(self.num)