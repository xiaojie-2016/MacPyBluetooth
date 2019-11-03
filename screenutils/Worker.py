import time

import bluetooth
from PyQt5.QtCore import QObject, pyqtSignal, QTimer


class BLEFinder(QObject):
    bleSignal = pyqtSignal(str)

    def __init__(self):
        super(BLEFinder, self).__init__()
        self._running = True

    def work(self):
        # while self._running:
        # self.search()
        # time.sleep(10)
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.search)  # 计时结束调用operate()方法
        self.timer.start(15000)  # 设置计时间隔并启动

    def search(selef):
        print("performing inquiry...")

        nearby_devices = bluetooth.discover_devices(
            duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

        # print("found %d devices" % len(nearby_devices))
        print(nearby_devices)
        #
        # for addr, name in nearby_devices:
        #     try:
        #         print("  %s - %s" % (addr, name))
        #     except UnicodeEncodeError:
        #         print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))
        # devices = bluetooth.discover_devices(duration=20, lookup_names=True)
        # return devices

    def stop(self):
        self.timer.stop()
