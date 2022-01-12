import random

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPen, QPolygon, QPainterPath, QBrush
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, \
    QPushButton
from pyqt_resource_helper import PyQtResourceHelper


class PolygonWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__border_width = 3
        self.__corner_length = 20
        self.__offset = 0
        self.__moving = False
        self.__initUi()

    def __initUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        closeBtn = QPushButton()
        closeBtn.clicked.connect(self.close)
        PyQtResourceHelper.setStyleSheet([closeBtn], ['style/button.css'])
        PyQtResourceHelper.setIcon([closeBtn], ['ico/close.png'])

        lay = QHBoxLayout()
        lay.setAlignment(Qt.AlignRight | Qt.AlignTop)
        lay.addWidget(closeBtn)
        lay.setContentsMargins(0, 3, 4, 0)

        menuBar = QWidget()
        menuBar.setLayout(lay)
        menuBar.setFixedHeight(self.__corner_length)  # menu bar height is supposed to be as same as corner length.

        lay = QVBoxLayout()
        lay.setAlignment(Qt.AlignTop)
        lay.addWidget(menuBar)
        lay.setContentsMargins(0, 0, 0, 0)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)

        self.setGeometry(20, 20, 300, 300)

    def paintEvent(self, e):
        painter = QPainter(self)
        brush = QBrush(QColor(50, 50, 50, 255))
        pen = QPen(QColor(Qt.darkGray), self.__border_width)
        painter.setPen(pen)
        painter.setBrush(brush)

        polygon = self.__getPolygon()
        painter.drawConvexPolygon(polygon)

        return super().paintEvent(e)

    def __getPolygon(self):

        # top left corner cut polygon
        p1 = QPolygon(self.rect(), True)
        p1.setPoint(0, QPoint(self.rect().topLeft().x(), self.rect().topLeft().y()+self.__corner_length))
        p1.setPoint(1, QPoint(self.rect().topLeft().x()+self.__corner_length, self.rect().topLeft().y()))
        p1.setPoint(2, self.rect().topRight())
        p1.setPoint(3, self.rect().bottomRight())
        p1.setPoint(4, self.rect().bottomLeft())

        # bottom right corner cut polygon
        p2 = QPolygon(self.rect(), True)
        p2.setPoint(0, self.rect().topLeft())
        p2.setPoint(1, self.rect().topRight())
        p2.setPoint(2, QPoint(self.rect().bottomRight().x(), self.rect().bottomRight().y()-self.__corner_length))
        p2.setPoint(3, QPoint(self.rect().bottomRight().x()-self.__corner_length, self.rect().bottomRight().y()))
        p2.setPoint(4, self.rect().bottomLeft())

        # get the intersection
        polygon = p1.intersected(p2)

        return polygon

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            p = e.pos()
            self.__offset = p
            self.__moving = True
        return super().mousePressEvent(e)

    def mouseMoveEvent(self, e):
        if self.__moving:
            self.move(e.globalPos() - self.__offset)
        return super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e):
        self.__moving = False
        return super().mouseReleaseEvent(e)

    def setBorderWidth(self, width: int):
        self.__border_width = width
        self.repaint()

    def setCornerLength(self, corner_length: int):
        self.__corner_length = corner_length
        self.repaint()