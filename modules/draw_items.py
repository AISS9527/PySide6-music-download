from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QListWidgetItem
from PySide6 import QtCore


class APP:
    @staticmethod
    def set_item(data):
        """设置搜索结果条目"""
        # 总Widget
        widget = QWidget()
        # 布局
        layout = QHBoxLayout()
        # 消息标签
        msg_label = QLabel('   '+data)
        msg_label.setStyleSheet('QLabel{'
                                'background: #db5a6b;'
                                'border: 2px;'
                                'border-radius: 12px;'
                                'font-size: 18px;'
                                'color: #ffffff;'
                                'font-family: "Microsoft YaHei";'
                                'text-align: center;}')
        # 添加组件
        layout.addWidget(msg_label)
        # 设置布局
        widget.setLayout(layout)
        return widget

    def get_item(self, data, listwidget):
        """使用条目"""
        item = QListWidgetItem()
        item.setSizeHint(QtCore.QSize(65, 65))
        widget = self.set_item(data)
        listwidget.addItem(item)
        listwidget.setItemWidget(item, widget)
