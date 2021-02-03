from PyQt5.QtWidgets import QVBoxLayout, QWidget, QRadioButton
from PyQt5 import QtCore


class add_verify(QWidget):
    change_status = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(add_verify, self).__init__(*args, **kwargs)
        # 确认身份 界面
        # 管理员身份
        self.radio_btn_admin = QRadioButton()
        self.radio_btn_admin.setText("我是管理员，来输入数据的")
        # 游客身份 二者只能选一个
        self.radio_btn_user = QRadioButton()
        self.radio_btn_user.setText("我是游客，就来看看")
        # 以垂直布局管理器管理 并设置为第一个界面
        radio_btn_layout = QVBoxLayout()
        self.radio_btn_widget = QWidget()
        radio_btn_layout.addWidget(self.radio_btn_admin)
        radio_btn_layout.addWidget(self.radio_btn_user)
        self.radio_btn_widget.setLayout(radio_btn_layout)
        

        self.radio_btn_user.toggled.connect(self.change_status)
        self.radio_btn_admin.toggled.connect(self.change_status)
