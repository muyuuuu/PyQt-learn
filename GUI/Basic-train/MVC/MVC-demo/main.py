import sys
from control.controller import Controll


if __name__ == "__main__":
    controller = Controll()
    # 退出主程序
    sys.exit(controller.run())