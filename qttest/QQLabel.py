from PyQt5.QtWidgets import QLabel

import UI_power
import extend_touxiang


class QQLabel(QLabel):
    def __init__(self, name=None, init=None):
        super(QLabel, self).__init__(init)
        self.name = name

    def mousePressEvent(self, event):
        if self.name == '头像':
            print('放大头像')
            self.add = self.styleSheet()
            self.add = self.add.replace('image', 'background-image')
            self.window = extend_touxiang.Ui_MainWindow(self.add)
            self.window.show()

        if self.name == '用户栏':
            if self.text().endswith('管理员'):
                self.window = UI_power.Ui_MainWindow()
                self.window.show()