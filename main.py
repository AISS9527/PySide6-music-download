from modules.all_mod import *


class MainWindow(RoundShadow, QWidget, Ui_Form):
    _startPos = None
    _endPos = None
    _isTracking = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(800, 570)
        self.setupUi(self)
        self.move_rect = QRect(0, 0, 800, 60)  # 移动窗口的矩形
        self.kugou = None
        self.song_list = None
        self._init_window__()

    def _init_window__(self):
        self.setMouseTracking(True)  # 鼠标跟踪
        self.import_qss()
        self.connect_signal()
        self.appfun = APP()
        self.msg_frame.close()
        self.setWindowIcon(QtGui.QPixmap('app.ico'))

    def import_kugou(self):
        """打开Web驱动器"""
        self.kugou = Download()

    def close_kugou(self):
        """关闭Web驱动器"""
        self.kugou.driver.close()

    def import_qss(self):
        qss_code = open('Theme/main_qss.qss', 'r')
        self.setStyleSheet(qss_code.read())
        qss_code.close()

    def get_song_name_list(self, key):
        self.song_list = self.kugou.search(key)
        for i in self.song_list:
            self.appfun.get_item(i, self.listWidget)

    def connect_signal(self):
        """连接信号"""
        self.close_button.clicked.connect(self.button_action)
        self.search_button.clicked.connect(self.button_action)
        self.mini_button.clicked.connect(self.button_action)
        self.download_button.clicked.connect(self.button_action)
        self.clear_button.clicked.connect(self.button_action)
        self.back_button.clicked.connect(self.button_action)

    def button_action(self):
        # 获取被点击按钮的名字
        btn = self.sender()
        btn_name = btn.objectName()
        # 退出按钮
        if btn_name == 'close_button':
            t2.start()  # 关闭酷狗
            self.close()  # 关闭窗口
        # 搜索按钮
        elif btn_name == 'search_button':
            # 如果没有条目的话
            if self.listWidget.count() == 0:
                key = self.search_lineEdit.text()
                if not key == '':
                    self.get_song_name_list(key)
            else:  # 有条目的先清除条目
                self.listWidget.clear()
                key = self.search_lineEdit.text()
                if not key == '':
                    self.get_song_name_list(key)
        # 最小化按钮
        elif btn_name == 'mini_button':
            self.showMinimized()
        # 下载按钮
        elif btn_name == 'download_button':
            b = self.listWidget.selectedIndexes()
            for ii in b:
                self.kugou.run(self.song_list, int(ii.row()))
                self.msg_frame.show()
        # 清除按钮
        elif btn_name == 'clear_button':
            self.listWidget.clear()
        # 确认按钮
        elif btn_name == 'back_button':
            self.msg_frame.close()

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        """鼠标移动事件"""
        if self._startPos:
            self._endPos = a0.pos() - self._startPos
            # 移动窗口
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, a0: QtGui.QMouseEvent):
        """鼠标按下事件"""
        # 根据鼠标按下时的位置判断是否在Rect范围内
        if self.move_rect.contains(a0.pos().x(), a0.pos().y()):
            # 判断鼠标按下的是左键
            if a0.button() == QtCore.Qt.LeftButton:
                self._isTracking = True
                # 记录初始位置
                self._startPos = QtCore.QPoint(a0.x(), a0.y())

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        """鼠标松开事件"""
        if a0.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    t = Thread(target=main.import_kugou)
    t.start()
    t2 = Thread(target=main.close_kugou)
    sys.exit(app.exec_())
