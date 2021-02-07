import sys, time
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QApplication, QPushButton


class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()

        layout = QHBoxLayout()
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        btn = QPushButton("点击")
        layout.addWidget(btn)
        btn.clicked.connect(self.count)

    def count(self):
        pass

if __name__ == '__main__':
    app = QApplication([])
    m = mainwindow()
    m.show()
    sys.exit(app.exec())