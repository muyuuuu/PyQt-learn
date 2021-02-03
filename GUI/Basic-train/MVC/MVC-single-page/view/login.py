from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QMessageBox, QLineEdit
from PyQt5 import QtCore


class MainWindow(QWidget):
    verifySignal = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.id_line = QLineEdit()
        self.id_line.setPlaceholderText("请输入账号")
        self.psd_line = QLineEdit()
        self.psd_line.setPlaceholderText("请输入密码")

        self.init()

    def init(self):

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.button = QPushButton("登录")
        layout.addWidget(self.button)

        layout.addWidget(self.id_line)
        layout.addWidget(self.psd_line)
    
        # 连接定义的信号
        self.button.clicked.connect(self.verify_emit)

    def verify_emit(self):
        self.verifySignal.emit()

    def verify_ok(self):
        QMessageBox.about(self, "密码正确", "已经登录")

    def verify_no(self):
        QMessageBox.about(self, "你犯了一个粗误", "请重新检查输入")
