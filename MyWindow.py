import bluetooth
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import QMainWindow

from screenutils.Worker import BLEFinder
from window import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        # self.worker = BLEFinder()
        # self.workerThread = QThread()
        # self.workerThread.moveToThread(self.workerThread)
        # self.worker.bleSignal.connect(self.updateList)
        # self.startButton.clicked.connect(self.startSearch)
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.search)  # 计时结束调用operate()方法
        self.timer.start(15000)  # 设置计时间隔并启动

    def search(selef):
        print("performing inquiry...")

        nearby_devices = bluetooth.discover_devices(
            duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

        print("found %d devices" % len(nearby_devices))
        # print(nearby_devices)
        #
        # for addr, name in nearby_devices:
        #     try:
        #         print("  %s - %s" % (addr, name))
        #     except UnicodeEncodeError:
        #         print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))
        # devices = bluetooth.discover_devices(duration=20, lookup_names=True)
        # return devices

    def updateList(self, devices):
        pass

    def startSearch(self):
        print('btn click')
        self.workerThread.started.connect(self.worker.work)
        self.workerThread.start()

if __name__ == '__main__':
    print("performing inquiry...")

    nearby_devices = bluetooth.discover_devices(
        duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

    print("found %d devices" % len(nearby_devices))