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
#from main import window


widgets = {
    "logo_robot": [],
    "robot_widget": [],
    "projectTitle": [],
    "startButton": [],
    "start_bnt_widget": [],
    "quitButton": [],
    "quit_bnt_widget": [],
    "backButton": []
}
grid = QGridLayout()


def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


# Transition functions
def start_detection():
    clear_widgets()
    frame2()


def goto_frame1():
    clear_widgets()
    frame1()


#*********************************************
#                  FRAME 1
#*********************************************
def frame1():
    #window.setWindowTitle("APA Project")
    robot_horizontalLayout = QHBoxLayout()
    robot_widget = QWidget()
    start_horizontalLayout = QHBoxLayout()
    start_bnt_widget = QWidget()
    quit_horizontalLayout = QHBoxLayout()
    quit_bnt_widget = QWidget()

    # Append widgets to list widgets
    widgets["robot_widget"].append(robot_widget)
    widgets["start_bnt_widget"].append(start_bnt_widget)
    widgets["quit_bnt_widget"].append(quit_bnt_widget)

    # Display LOGO
    movie = QMovie(u"Icons/project_robot.gif")
    logo_robot = QLabel()
    logo_robot.setMovie(movie)
    logo_robot.setAlignment(Qt.AlignmentFlag.AlignCenter)
    logo_robot.setMaximumHeight(100)
    logo_robot.setScaledContents(True)
    logo_robot.setFixedSize(375, 250)
    movie.start()
    widgets["logo_robot"].append(logo_robot)

    # Display Project Title
    projectTitle = QLabel("Computer Vision Project 👨‍💻💻🖥️")
    projectTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
    projectTitle.setStyleSheet(
        "font-size: 50px;"
        "color: #14171A;"
        "margin: 50px 0 0 0;"
    )
    widgets["projectTitle"].append(projectTitle)

    # Start button widget
    startButton = QPushButton("START")
    startButton.setObjectName("startButton")
    startButton.setCursor(QCursor(Qt.PointingHandCursor))
    startButton.setStyleSheet(
        "#startButton{width: 300px;"
        "height: 50px;"
        "margin: 150px 0 0 0;"
        "padding: 5px 0;"
        "background-color: '#FFFFFF';"
        "border: 3px solid '#1DA1F2';"
        "border-radius: 30px;"
        "font-size: 28px;"
        "color: '#657786';}"
        # Hover effect
        "#startButton:hover{background-color: '#1DA1F2';"
        "border: none;"
        "color: '#FFFFFF';}"
    )
    startButton.setMaximumWidth(500)
    startButton.clicked.connect(start_detection)
    startButton.clicked.connect(movie.deleteLater)
    widgets["startButton"].append(startButton)

    # Quit button widget
    quitButton = QPushButton("QUIT")
    quitButton.setObjectName("quitButton")
    quitButton.setCursor(QCursor(Qt.PointingHandCursor))
    quitButton.setStyleSheet(
        "#quitButton{width: 300px;"
        "height: 50px;"
        "margin: 0 0 50px 0;"
        "padding: 5px 0;"
        "background-color: '#FFFFFF';"
        "border: 3px solid '#DD0031';"
        "border-radius: 30px;"
        "font-size: 28px;"
        "color: '#657786';}"
        # Hover effect
        "#quitButton:hover{background-color: '#DD0031';"
        "border: none;"
        "color: '#FFFFFF';}"
    )
    quitButton.setMaximumWidth(500)
    widgets["quitButton"].append(quitButton)

    # Vertical spacer
    verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    # Horizontal spacer
    horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    grid.addItem(verticalSpacer, 0, 0)
    robot_horizontalLayout.addItem(horizontalSpacer)
    robot_horizontalLayout.addWidget(widgets["logo_robot"][-1])
    robot_horizontalLayout.addItem(horizontalSpacer)
    robot_widget.setLayout(robot_horizontalLayout)
    grid.addWidget(widgets["robot_widget"][-1], 1, 0)
    grid.addItem(verticalSpacer, 2, 0)
    grid.addWidget(widgets["projectTitle"][-1], 3, 0)
    start_horizontalLayout.addItem(horizontalSpacer)
    start_horizontalLayout.addWidget(widgets["startButton"][-1])
    start_horizontalLayout.addItem(horizontalSpacer)
    start_bnt_widget.setLayout(start_horizontalLayout)
    grid.addWidget(widgets["start_bnt_widget"][-1], 4, 0)
    quit_horizontalLayout.addItem(horizontalSpacer)
    quit_horizontalLayout.addWidget(widgets["quitButton"][-1])
    quit_horizontalLayout.addItem(horizontalSpacer)
    quit_bnt_widget.setLayout(quit_horizontalLayout)
    grid.addWidget(widgets["quit_bnt_widget"][-1], 5, 0)
    grid.addItem(verticalSpacer, 6, 0)


#*********************************************
#                  FRAME 2
#*********************************************
def frame2():
    #window.setWindowTitle("Detection Algorithms")
    back_horizontalLayout = QHBoxLayout()
    back_widget = QWidget()
    image_Layout = QGridLayout()
    image_grid = QWidget()

    image1 = QLabel()
    image2 = QLabel()
    image3 = QLabel()

    image1.setObjectName("eye_detection")
    image2.setObjectName("color_detection")
    image3.setObjectName("object_detection")

    image1.setPixmap(QPixmap(u"Photos\eye_detection.png"))
    image2.setPixmap(QPixmap(u"Photos\color_detection.png").scaled(200, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation))
    image3.setPixmap(QPixmap(u"Photos\object_detection.png").scaled(200, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation))

    image1.setScaledContents(True)
    image2.setScaledContents(True)
    image3.setScaledContents(True)

    image1.setAlignment(Qt.AlignmentFlag.AlignCenter)
    image2.setAlignment(Qt.AlignmentFlag.AlignCenter)
    image3.setAlignment(Qt.AlignmentFlag.AlignCenter)

    image1.setStyleSheet(
        "#eye_detection{"
        "margin: 15px;}"
    )
    image2.setStyleSheet(
        "#eye_detection{"
        "margin: 15px;}"
    )
    image3.setStyleSheet(
        "#eye_detection{"
        "margin: 15px;}"
    )

    button1 = QPushButton("Detect")
    button2 = QPushButton("Detect")
    button3 = QPushButton("Detect")

    button1.setObjectName("eye_detection_btn")
    button2.setObjectName("color_detection_btn")
    button3.setObjectName("object_detection_btn")

    button1.setStyleSheet(
        "#eye_detection_btn{height: 42px;"
        "margin: 15px;"
        "padding: 5px 0;"
        "background-color: '#FFFFFF';"
        "border: 3px solid '#1DA1F2';"
        "border-radius: 26px;"
        "font-size: 28px;"
        "color: '#657786';}"
        # Hover effect
        "#eye_detection_btn:hover{background-color: '#1DA1F2';"
        "border: none;"
        "color: '#FFFFFF';}"
    )
    button2.setStyleSheet(
        "#color_detection_btn{height: 42px;"
        "margin: 15px;"
        "padding: 5px 0;"
        "background-color: '#FFFFFF';"
        "border: 3px solid '#1DA1F2';"
        "border-radius: 26px;"
        "font-size: 28px;"
        "color: '#657786';}"
        # Hover effect
        "#color_detection_btn:hover{background-color: '#1DA1F2';"
        "border: none;"
        "color: '#FFFFFF';}"
    )
    button3.setStyleSheet(
        "#object_detection_btn{height: 42px;"
        "margin: 15px;"
        "padding: 5px 0;"
        "background-color: '#FFFFFF';"
        "border: 3px solid '#1DA1F2';"
        "border-radius: 26px;"
        "font-size: 28px;"
        "color: '#657786';}"
        # Hover effect
        "#object_detection_btn:hover{background-color: '#1DA1F2';"
        "border: none;"
        "color: '#FFFFFF';}"
    )



    backButton = QPushButton("START")
    backButton.setObjectName("backButton")
    backButton.setCursor(QCursor(Qt.PointingHandCursor))
    backButton.setStyleSheet(
        "#backButton{"
        "background-color: '#FFFFFF';"
        "border: 3px solid '#1DA1F2';"
        "border-radius: 15px;"
        "font-size: 28px;"
        "color: '#657786';}"
        # Hover effect
        "#backButton:hover{background-color: '#1DA1F2';"
        "border: none;"
        "color: '#FFFFFF';}"
    )

    backButton.setFixedSize(60, 60)
    back_widget.setFixedHeight(70)
    backButton.clicked.connect(goto_frame1)
    widgets["backButton"].append(backButton)

    # Vertical spacer
    verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    # Horizontal spacer
    horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
    
    grid.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding), 0,0)

    image_Layout.addItem(QSpacerItem(250, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed), 0, 0)
    image_Layout.addWidget(image1, 0, 1)
    image_Layout.addWidget(image2, 0, 2)
    image_Layout.addWidget(image3, 0, 3)
    image_Layout.addItem(QSpacerItem(250, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed), 0, 4)
    image_Layout.addItem(QSpacerItem(250, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed), 1, 0)
    image_Layout.addWidget(button1, 1, 1)
    image_Layout.addWidget(button2, 1, 2)
    image_Layout.addWidget(button3, 1, 3)
    image_Layout.addItem(QSpacerItem(250, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed), 1, 4)
    image_grid.setLayout(image_Layout)
    grid.addWidget(image_grid, 1, 0)

    #grid.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding), 2,0)
    back_horizontalLayout.addItem(QSpacerItem(15, 15, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
    back_horizontalLayout.addWidget(backButton)
    back_horizontalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
    back_widget.setLayout(back_horizontalLayout)
    grid.addWidget(back_widget, 2, 0)
