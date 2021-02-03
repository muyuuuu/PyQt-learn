'''
File: test.py
Project: test
File Created: Wednesday, 3rd February 2021 4:52:53 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Wednesday, 3rd February 2021 5:22:11 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2021 XDU, XDU
-----------
Description: 自定义信号与自定义槽函数演示
'''

from PyQt5.QtCore import QObject, pyqtSignal

# 信号对象
class QSignal(QObject):
    # 定义信号
    # 在类创建时定义，不能在类创建后作为类的属性而添加
    # 指定信号传递参数的数量，类型等
    send_msg = pyqtSignal(str, str)

    def __init__(self):
        super(QSignal, self).__init__()

    def run(self):
        # 信号发射
        self.send_msg.emit('First arg', 'Second arg')

# 槽对象
class QSlot(QObject):
    def __init__(self):
        super(QSlot, self).__init__()

    def get(self, *args):
        # 信号接收
        print("Get message =>" + args[0], args[1], sep=', ')

if __name__ == '__main__':
    send = QSignal()
    slot = QSlot()

    # 将信号与槽函数绑定
    send.send_msg.connect(slot.get)
    # 外部调用 发射信号
    send.run()
    # 信号与槽解除关联
    send.send_msg.disconnect(slot.get)
    send.run()