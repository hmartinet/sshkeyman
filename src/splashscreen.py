# -*- coding: utf-8 -*-

from PyQt4.QtCore import Qt, QPointF
from PyQt4.QtGui import QSplashScreen, QPixmap, QPainter, QPen, QBrush, QColor

class SplashScreen(QSplashScreen):
    
    progress = 0.0
    message = 'Loading...'
    
    def __init__(self):
        QSplashScreen.__init__(self, QPixmap('media/splash.png'), Qt.WindowStaysOnTopHint)
        self.show()
        
    def setProgress(self, value, message=None):
        self.progress = value
        if message:
            self.message = message
        self.repaint()
        
    def paintEvent(self, paintEvent):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white))
        painter.drawText(QPointF(14, self.height()-16), str(self.message))
        painter.setPen(QPen(QBrush(QColor(58, 93, 208)), 8))
        if self.progress > 0.0:
            painter.drawLine(0, self.height()-4, self.progress * self.width(), self.height()-4)