class Controller(object):
    def __init__(self, verify_page, left_btn):
        verify_page.change_status.connect(self.check_status)
        self._verify_page = verify_page
        self.left_btn = left_btn
        self.init()

    def init(self):
        self._verify_page.change_status.connect(self.check_status)

    def check_status(self):
        if self._verify_page.radio_btn_admin.isChecked():
            self.left_btn.user_btn.setEnabled(True)
        else:
            self.left_btn.user_btn.setEnabled(False)