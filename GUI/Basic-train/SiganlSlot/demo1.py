'''
File: a.py
Project: test
File Created: Wednesday, 3rd February 2021 5:03:21 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Wednesday, 3rd February 2021 5:21:28 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2021 XDU, XDU
-----------
Description: 内置信号绑定自定义槽函数
'''
import sys
from functools import partial
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    btn_signal = pyqtSignal()
    def __init__(self):
        super(MainWindow, self).__init__()

        a = QPushButton("退出")
        a.clicked.connect(partial(self.btn_clicked, 1))
        self.btn_signal.connect(self.close)

        self.setWindowTitle("演示")

        main_widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(a)
        main_widget.setLayout(layout)
        # QMainWindow 不能设置布局
        self.setCentralWidget(main_widget)

    def btn_clicked(self, n):
        print(n)
        self.btn_signal.emit()

    def close(self):
        app = QApplication.instance()
        app.quit()


if __name__ == "__main__":
    # 在shell中执行
    app = QApplication(sys.argv)
    mywin = MainWindow()
    mywin.show()
    # 开始主循环，直到退出
    sys.exit(app.exec())