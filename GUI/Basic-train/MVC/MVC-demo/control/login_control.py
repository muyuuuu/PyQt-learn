class Controller(object):
    def __init__(self, login_page, stu_id, stu_psd):
        self._login_page = login_page
        self._stu_id = stu_id
        self._stu_psd = stu_psd
        self._login_page.login_signal.connect(self.login)

    def login(self):
        id = self._login_page.user_line.text()
        psd = self._login_page.psd_line.text()

        if id == self._stu_id and psd == self._stu_psd:
            self._login_page.verify_ok()
        else:
            self._login_page.verify_no()
