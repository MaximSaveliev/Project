import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt6.QtGui import QPixmap
from PyQt6 import QtGui, QtCore, sip
from PyQt6.QtGui import QCursor
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QMovie,
                           QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QGridLayout, QLabel,
                               QMainWindow, QPushButton, QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout, QWidget, QFileDialog)
from frame_functions import frame1, frame2, grid


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    icon = QIcon()
    icon.addFile(u"Icons/Icon.png", QSize(), QIcon.Normal, QIcon.Off)
    window.setWindowIcon(icon)
    window.resize(1200, 900)
    window.setStyleSheet("background: #FFFFFF;")

    frame1()

    window.setLayout(grid)

    window.show()
    sys.exit(app.exec())
