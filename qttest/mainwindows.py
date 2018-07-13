import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import login
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    UI = login.Ui_MainWindow()
    UI.show()
    sys.exit(app.exec_())