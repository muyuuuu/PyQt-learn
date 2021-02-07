'''
File: th.py
Project: demo
File Created: Friday, 5th February 2021 6:13:30 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Friday, 5th February 2021 6:21:55 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2021 XDU, XDU
-----------
Description: 模拟 IO
'''
import sys, time
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QWidget, QApplication, 
                             QHBoxLayout)
from PyQt5.QtCore import QThread, pyqtSignal


class Worker(QThread):
    # 自定义信号
    signal_out = pyqtSignal(str)
    def __init__(self, working):
        super(Worker, self).__init__()
        self.working = working
        self.num = 0
        # 结束信号的触发
        self.finished.connect(self.finish)

    def finish(self):
        print('finish')

    def run(self):
        # while 持续发送
        while self.working == True:
            string = "Index " + str(self.num)
            self.num += 1
            self.signal_out.emit(string)
            self.sleep(1)
            if self.num != 0 and self.num % 2 == 0:
                self.signal_out.emit("stop")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.text = QTextEdit()
        layout = QHBoxLayout()
        layout.addWidget(self.text)
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        self.worker = Worker(working=True)
        self.start()
        self.worker.signal_out.connect(self.display)

    def display(self, string):
        if string == 'stop':
            self.text.clear()
            # 线程结束后，被这个线程阻塞的线程都会被唤醒
            self.worker.working = False
            self.worker.quit()
            # 强制结束进程的执行，但不推荐
            # self.worker.terminate()
        else:
            QApplication.processEvents()
            self.text.append(string)

    def start(self):
        # 启动线程
        # 自动调用类内的 run 方法
        self.worker.start()

if __name__ == "__main__":
    q = QApplication([])
    m = MainWindow()
    m.show()
    sys.exit(q.exec())
