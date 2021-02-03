from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget
from PyQt5 import QtCore


class add_btn(QWidget):
    verify_signal = QtCore.pyqtSignal()
    login_signal = QtCore.pyqtSignal()

    def __init__(self, left_frame, right_layout):
        super(add_btn, self).__init__()

        self.right_layout = right_layout

        # 登录按钮 用于验证身份
        button_layout = QVBoxLayout(left_frame)
        self.verifyid_btn = QPushButton("确认身份")
        button_layout.addWidget(self.verifyid_btn)
        # 输入用户名　密码按钮
        # 因为在radiobutton中需要选择是否为管理员
        # 因此需要 确定某些按钮是否可用，所以，设置为self方便子函数的调用
        self.user_btn = QPushButton("登录")
        self.user_btn.setEnabled(False)
        button_layout.addWidget(self.user_btn)

        self.verifyid_btn.clicked.connect(self.verify_signal)
        self.user_btn.clicked.connect(self.login_signal)

    def show_verified_page(self):
        self.right_layout.setCurrentIndex(0)

    def show_login_page(self):
        self.right_layout.setCurrentIndex(1)