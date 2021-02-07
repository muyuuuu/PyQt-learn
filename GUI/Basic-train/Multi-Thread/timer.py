import sys, time
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QWidget, 
                             QHBoxLayout)
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: white')

        self.label = QLabel()
        # 居中对齐
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.loading = QMovie("images/loading.gif")
        self.label.setMovie(self.loading)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.loading_start()
        self.setLayout(self.layout)

        # 定时器
        self.t = QTimer()
        self.t.start(8000)
        self.t.timeout.connect(self.loading_end)

    def loading_end(self):
        self.t.stop()
        self.loading.stop()
        time.sleep(0.2)
        self.label.clear()

    def loading_start(self):
        self.loading.start()
        # self.loading.stop()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        W = MainWidget()
        self.setCentralWidget(W)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())