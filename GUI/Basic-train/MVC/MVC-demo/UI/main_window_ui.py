from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QFrame, QStackedLayout, QSplitter,
                             QGridLayout, QWidget)
from PyQt5.QtCore import Qt
import qdarkstyle
from UI import leftbtn_ui, verify_ui, login_ui


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        # 设置窗口名称
        self.setWindowTitle("一个 MVC 实例")

        # 设置状态栏
        self.status = self.statusBar()
        self.status.showMessage("写着玩的~")

        # 设置初始化的窗口大小
        self.setFixedSize(600, 400)

        # 设置初始化的窗口位置
        self.center()

        # 设置整体布局 左右显示
        pagelayout = QGridLayout()

        """
        此处完成布局页面的基本功能
        布局分为左侧和右侧，左侧为按钮，右侧为堆栈布局，完成鼠标点击的页面切换功能
        最后两个布局部署在splitter中，完成页面内部拖拉界面可变大小
        """

        # 创建左侧主窗口
        left_frame = QFrame(self)
        # 绘制矩形面板
        left_frame.setFrameShape(QFrame.StyledPanel)

        right_frame = QFrame(self)
        right_frame.setFrameShape(QFrame.StyledPanel)
        # 右边显示为stack布局 即点击按钮，右侧会加载不同的页面
        self.right_layout = QStackedLayout(right_frame)

        # 左侧按钮添加
        self.Btn = leftbtn_ui.add_btn(left_frame, self.right_layout)

        self.verify_page = verify_ui.add_verify()
        self.right_layout.addWidget(self.verify_page.radio_btn_widget)
        
        self.login_page = login_ui.add_login()
        self.right_layout.addWidget(self.login_page.login_widget)

        # 二分界面，可拖动
        self.splitter1 = QSplitter(Qt.Vertical)
        # left_frame.setFixedHeight(280)
        self.splitter1.addWidget(left_frame)
        self.splitter1.setMinimumWidth(150)
        self.splitter2 = QSplitter(Qt.Horizontal)
        self.splitter2.addWidget(self.splitter1)
        self.splitter2.setMinimumWidth(250)
        #　添加右侧的布局
        self.splitter2.addWidget(right_frame)

        # 窗口部件添加布局
        widget = QWidget()
        pagelayout.addWidget(self.splitter2)
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def center(self):
        """
        获取桌面长宽  获取窗口长宽 计算位置 移动
        """
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))
