#!/bin/bash
# -*- coding: UTF-8 -*-
import sys, pandas
import PyQt5
import numpy as np
# 基本控件都在这里面
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QStyleFactory, QWidget
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from mainwidget import Ui_Form
from mainwindow import Ui_MainWindow

from qtpandas.views.DataTableView import DataTableWidget
from qtpandas.models.DataFrameModel import DataFrameModel
# 继承主窗口 Qmainwindow 和 自己画的界面 Ui_MainWindow
class MyMainWidget(QWidget, Ui_Form):

    def __init__(self, parent = None):
        super(MyMainWidget, self).__init__(parent)
        self.setupUi(self)

        self.setLayout(self.gridLayout)

        # 退出窗口
        self.quit_btn.clicked.connect(self.quit_act)

        # qtpandas
        model = DataFrameModel() # 空模型那个用于存储和处理数据
        # print(type(self.widget_2))
        self.widget_2.setViewModel(model)
        data = {
            'A': [10, 11, 12],
            'B': [12, 11, 10],
            'C': ['a', 'b', 'c']
        }
        self.df = pandas.DataFrame(data)
        self.df['A'] = self.df['A'].astype(np.int8) # 委托，规定某一列的类型
        model.setDataFrame(self.df)

        # 保存数据
        self.quit_btn_7.clicked.connect(self.save_data)

    def save_data(self):
        self.df.to_csv('data.csv')

    def quit_act(self):
        # sender 是发送信号的对象
        sender = self.sender()
        print(sender.text() + '键被按下')
        qApp = QApplication.instance()
        qApp.quit()


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        q = MyMainWidget()
        self.setCentralWidget(q)

        # 设置窗口透明
        self.setWindowOpacity(0.9)

        # self.resize(1000, 700)

        # 默认的状态栏
        # 可以设置其他按钮点击 参考多行文本显示 然而不行 
        self.status = self.statusBar()
        self.status.showMessage("你在主页面～")
        
        # 标题栏
        self.setWindowTitle("建模协会录入信息")

        # 窗口居中
        self.center()

    def center(self):
        '''
        获取桌面长宽
        获取窗口长宽
        移动
        '''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

if __name__ == "__main__":
    # 在shell中执行
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    # 开始主循环，直到退出
    sys.exit(app.exec())
