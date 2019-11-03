import time

import bluetooth
from PyQt5.QtCore import QThread, pyqtSignal


class BluetoothThread(QThread):
    singal = pyqtSignal(str)

    def __init__(self):
        super(BluetoothThread, self).__init__()

    def search(selef):
        print("performing inquiry...")

        nearby_devices = bluetooth.discover_devices(
            duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

        print("found %d devices" % len(nearby_devices))

        for addr, name in nearby_devices:
            try:
                print("  %s - %s" % (addr, name))
            except UnicodeEncodeError:
                print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))
        # devices = bluetooth.discover_devices(duration=20, lookup_names=True)
        # return devices

    def run(self):
        while True:
            self.search()
            # results = search()
            # if (results != None):
            #     for addr, name in results:
            #         print("{0} - {1}".format(addr, name))
            # endfor
            # endif
            time.sleep(30)
        # endwhile
