import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QMessageBox, 
                             QLineEdit, QApplication)

# View
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

# model
class Student(object):

    def __init__(self):
        self.name = "aaa"
        self.password = "aaa"

# control
class LoginControll(object):

    def __init__(self):
        # 不需要从命令行输入参数
        self._app = QApplication([])
        self._model = Student()
        self._view = MainWindow()
        self.init()

    def init(self):
        self._view.verifySignal.connect(self.verify_user)

    def verify_user(self):
        id_ = self._view.id_line.text()
        psd_ = self._view.psd_line.text()

        if id_ == self._model.name and psd_ == self._model.password:
            self._view.verify_ok()
        else:
            self._view.verify_no()

    def run(self):
        self._view.show()
        # 事件循环，直到应用退出
        return self._app.exec_()

# main.py
if __name__ == "__main__":
    login_control_ = LoginControll()
    # 退出主程序
    sys.exit(login_control_.run())