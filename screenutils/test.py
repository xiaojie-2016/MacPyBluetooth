import threading

import bluetooth
from PyQt5 import QtBluetooth
from PyQt5.QtBluetooth import QBluetoothDeviceDiscoveryAgent
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Worker(QThread):
    sinOut = pyqtSignal(str) # 自定义信号，执行run()函数时，从相关线程发射此信号

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        print(threading.enumerate())
        # while self.working == True:
        #     print("performing inquiry...")
        #
        #     nearby_devices = bluetooth.discover_devices(
        #         duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
        #
        #     print("found %d devices" % len(nearby_devices))
        #     # print(nearby_devices)
        #     # file_str = 'File index {0}'.format(self.num) # str.format()
        #     # self.num += 1
        #     # 发出信号
        #     # self.sinOut.emit(file_str)
        #
        #     # 线程休眠2秒
        #     self.sleep(20)


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.setWindowTitle("QThread 例子")

        # 布局管理
        self.listFile = QListWidget()
        self.btnStart = QPushButton('开始')
        layout = QGridLayout(self)
        layout.addWidget(self.listFile, 0, 0, 1, 2)
        layout.addWidget(self.btnStart, 1, 1)

        # 连接开始按钮和槽函数
        self.btnStart.clicked.connect(self.slotStart)

        # 创建新线程，将自定义信号sinOut连接到slotAdd()槽函数
        self.thread = Worker()
        self.thread.sinOut.connect(self.slotAdd)

    # 开始按钮按下后使其不可用，启动线程
    def slotStart(self):
        self.btnStart.setEnabled(False)
        self.thread.start()

    # 在列表控件中动态添加字符串条目
    def slotAdd(self, file_inf):
        self.listFile.addItem(file_inf)

import Adafruit_BluefruitLE
import Adafruit_BluefruitLE.services

def find():
    Adafruit_BluefruitLE.get_provider()
    print(QBluetoothDeviceDiscoveryAgent().discoveredDevices())

if __name__ == "__main__":
    find()
    # app = QApplication(sys.argv)
    # demo = MainWidget()
    # demo.show()
    # sys.exit(app.exec_())
