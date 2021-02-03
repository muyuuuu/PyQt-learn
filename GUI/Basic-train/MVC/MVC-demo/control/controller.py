import sys
from PyQt5.QtWidgets import QApplication
from model.model import Student
from UI.main_window_ui import MainWindow
from control import verify_control, leftbtn_control, login_control


class Controll(object):

    def __init__(self):
        # 不需要从命令行输入参数
        # 初始换应用
        self._app = QApplication([])
        # 初始化模型
        self._stu = Student()
        # 初始化试图
        self._view = MainWindow()
        self.init()

    # 各个子 controller
    def init(self):
        self.verify_ui_controller = verify_control.Controller(self._view.verify_page, self._view.Btn)
        self.left_btn_controller = leftbtn_control.Controller(self._view.Btn)
        self.login_controller = login_control.Controller(self._view.login_page, self._stu.name, self._stu.password)

    def run(self):
        self._view.show()
        # 事件循环，直到应用退出
        return self._app.exec()
