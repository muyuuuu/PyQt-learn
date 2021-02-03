import sys
from control import login_control


if __name__ == "__main__":
    login_control_ = login_control.LoginControll()
    # 退出主程序
    sys.exit(login_control_.run())