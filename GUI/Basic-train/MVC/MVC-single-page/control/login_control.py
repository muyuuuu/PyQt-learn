import sys
import view.login as V
import model.model as M
from PyQt5.QtWidgets import QApplication


class LoginControll(object):

    def __init__(self):
        # 不需要从命令行输入参数
        self._app = QApplication([])
        self._model = M.Student()
        self._view = V.MainWindow()
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
