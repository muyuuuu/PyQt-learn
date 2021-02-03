from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QWidget, QMessageBox
from PyQt5 import QtCore


class add_login(QWidget):
    login_signal = QtCore.pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(add_login, self).__init__(*args, **kwargs)
    
        self.user_line = QLineEdit()
        self.user_line.setPlaceholderText("请输入账号：(游客可直接查询，请勿登录)")
        self.user_line.setFixedHeight(40)
        self.psd_line = QLineEdit()
        self.psd_line.setPlaceholderText("请输入密码：")
        self.psd_line.setEchoMode(QLineEdit.Password)
        self.psd_line.setFixedHeight(40)
        # 帐号密码的布局
        login_layout = QVBoxLayout()
        login_btn_layout = QHBoxLayout()
        login_btn_cancel = QPushButton("取消")
        self.login_btn_confirm = QPushButton("确认")
        # 按钮的布局
        login_btn_layout.addWidget(login_btn_cancel)
        login_btn_layout.addWidget(self.login_btn_confirm)
        # 添加全部元素的布局
        login_layout.addWidget(self.user_line)
        login_layout.addWidget(self.psd_line)
        login_layout.addLayout(login_btn_layout)
        self.login_widget = QWidget()
        self.login_widget.setLayout(login_layout)
        self.login_btn_confirm.clicked.connect(self.login)

    def login(self):
        self.login_signal.emit()

    def verify_ok(self):
        QMessageBox.about(self, "密码正确", "已经登录")

    def verify_no(self):
        QMessageBox.about(self, "你犯了一个粗误", "请重新检查输入")