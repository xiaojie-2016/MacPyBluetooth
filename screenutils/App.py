import subprocess
import sys
import time

import bluetooth
from PyQt5 import QtWidgets

from MyWindow import MyWindow
from screenutils.BluetoothSearchThread import BluetoothThread
from window import Ui_MainWindow


def closeScreen():
    subprocess.call("service apache2 status", shell=True)


def updateVeiw():
    pass

def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)

    # bThread = BluetoothThread()
    # bThread.start()
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui = MyWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # ui.hhh()
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    # search()
    # result = search()
    # print(result)
    show_MainWindow()


