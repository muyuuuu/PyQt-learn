import sys, time
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QWidget, 
                             QHBoxLayout)
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt


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

    def loading_start(self):
        self.loading.start()
        # self.loading.stop()
        time.sleep(2)
        self.loading.setPaused(True)
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