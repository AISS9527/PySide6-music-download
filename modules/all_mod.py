import sys

from PySide6.QtCore import QRectF, QRect, QThread
from PySide6.QtGui import Qt, QPainterPath, QBrush, QPainter, QColor
from PySide6.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel, QPushButton, QListWidgetItem, QFrame

from PySide6 import QtCore, QtGui
from modules.round_window import RoundShadow
from web import Download
from threading import Thread
from MainWindow.main import Ui_Form
from draw_items import APP
