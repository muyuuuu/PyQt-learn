class Controller(object):
    def __init__(self, left_btn):
        self._left_btn = left_btn

        self._left_btn.verify_signal.connect(self._left_btn.show_verified_page)
        self._left_btn.login_signal.connect(self._left_btn.show_login_page)
