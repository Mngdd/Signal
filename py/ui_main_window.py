# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowYVzgYD.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLCDNumber, QLabel, QLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1103, 596)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 10, 1041, 426))
        self.InputLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.InputLayout.setObjectName(u"InputLayout")
        self.InputLayout.setContentsMargins(0, 0, 0, 0)
        self.ObjInputGrid = QGridLayout()
        self.ObjInputGrid.setObjectName(u"ObjInputGrid")
        self.ObjInputGrid.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.AdditionalInputs = QVBoxLayout()
        self.AdditionalInputs.setObjectName(u"AdditionalInputs")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.MidLayoutRAD = QVBoxLayout()
        self.MidLayoutRAD.setObjectName(u"MidLayoutRAD")
        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)

        self.MidLayoutRAD.addWidget(self.label_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.RAD_ENERGY = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.RAD_ENERGY.setObjectName(u"RAD_ENERGY")
        self.RAD_ENERGY.setDecimals(4)
        self.RAD_ENERGY.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_8.addWidget(self.RAD_ENERGY)


        self.MidLayoutRAD.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_16.addLayout(self.MidLayoutRAD)

        self.line_7 = QFrame(self.verticalLayoutWidget_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_7)

        self.RightLayoutRAD = QVBoxLayout()
        self.RightLayoutRAD.setObjectName(u"RightLayoutRAD")
        self.label_9 = QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.RightLayoutRAD.addWidget(self.label_9)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.RAD_DIR_X = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.RAD_DIR_X.setObjectName(u"RAD_DIR_X")
        self.RAD_DIR_X.setDecimals(4)
        self.RAD_DIR_X.setMaximum(1000.000000000000000)

        self.horizontalLayout_15.addWidget(self.RAD_DIR_X)

        self.RAD_DIR_Y = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.RAD_DIR_Y.setObjectName(u"RAD_DIR_Y")
        self.RAD_DIR_Y.setDecimals(4)
        self.RAD_DIR_Y.setMaximum(1000.000000000000000)

        self.horizontalLayout_15.addWidget(self.RAD_DIR_Y)

        self.RAD_DIR_Z = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.RAD_DIR_Z.setObjectName(u"RAD_DIR_Z")
        self.RAD_DIR_Z.setDecimals(4)
        self.RAD_DIR_Z.setMaximum(1000.000000000000000)

        self.horizontalLayout_15.addWidget(self.RAD_DIR_Z)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)


        self.RightLayoutRAD.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_16.addLayout(self.RightLayoutRAD)


        self.AdditionalInputs.addLayout(self.horizontalLayout_16)

        self.line_5 = QFrame(self.verticalLayoutWidget_3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.AdditionalInputs.addWidget(self.line_5)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.RightLayoutOBJ = QVBoxLayout()
        self.RightLayoutOBJ.setObjectName(u"RightLayoutOBJ")
        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.RightLayoutOBJ.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.OBJ_RADIUS = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.OBJ_RADIUS.setObjectName(u"OBJ_RADIUS")
        self.OBJ_RADIUS.setDecimals(4)
        self.OBJ_RADIUS.setMaximum(100000000000.000000000000000)

        self.horizontalLayout.addWidget(self.OBJ_RADIUS)


        self.RightLayoutOBJ.addLayout(self.horizontalLayout)


        self.horizontalLayout_18.addLayout(self.RightLayoutOBJ)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_4)


        self.AdditionalInputs.addLayout(self.horizontalLayout_18)

        self.line_6 = QFrame(self.verticalLayoutWidget_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.AdditionalInputs.addWidget(self.line_6)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.RightLayoutREC = QVBoxLayout()
        self.RightLayoutREC.setObjectName(u"RightLayoutREC")
        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.RightLayoutREC.addWidget(self.label_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.REC_CE = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.REC_CE.setObjectName(u"REC_CE")
        self.REC_CE.setDecimals(4)
        self.REC_CE.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_5.addWidget(self.REC_CE)


        self.RightLayoutREC.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_17.addLayout(self.RightLayoutREC)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_6)


        self.AdditionalInputs.addLayout(self.horizontalLayout_17)


        self.ObjInputGrid.addLayout(self.AdditionalInputs, 0, 4, 1, 1)

        self.CoordsInputs = QVBoxLayout()
        self.CoordsInputs.setObjectName(u"CoordsInputs")
        self.LeftLayoutRAD = QVBoxLayout()
        self.LeftLayoutRAD.setObjectName(u"LeftLayoutRAD")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)


        self.LeftLayoutRAD.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.RAD_COORD_X = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.RAD_COORD_X.setObjectName(u"RAD_COORD_X")
        self.RAD_COORD_X.setDecimals(4)
        self.RAD_COORD_X.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_10.addWidget(self.RAD_COORD_X)

        self.RAD_COORD_Y = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.RAD_COORD_Y.setObjectName(u"RAD_COORD_Y")
        self.RAD_COORD_Y.setDecimals(4)
        self.RAD_COORD_Y.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_10.addWidget(self.RAD_COORD_Y)

        self.RAD_COORD_Z = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.RAD_COORD_Z.setObjectName(u"RAD_COORD_Z")
        self.RAD_COORD_Z.setDecimals(4)
        self.RAD_COORD_Z.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_10.addWidget(self.RAD_COORD_Z)


        self.LeftLayoutRAD.addLayout(self.horizontalLayout_10)


        self.CoordsInputs.addLayout(self.LeftLayoutRAD)

        self.line_4 = QFrame(self.verticalLayoutWidget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.CoordsInputs.addWidget(self.line_4)

        self.LeftLayoutOBJ = QVBoxLayout()
        self.LeftLayoutOBJ.setObjectName(u"LeftLayoutOBJ")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.LeftLayoutOBJ.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.OBJ_COORD_X = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.OBJ_COORD_X.setObjectName(u"OBJ_COORD_X")
        self.OBJ_COORD_X.setDecimals(4)
        self.OBJ_COORD_X.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_7.addWidget(self.OBJ_COORD_X)

        self.OBJ_COORD_Y = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.OBJ_COORD_Y.setObjectName(u"OBJ_COORD_Y")
        self.OBJ_COORD_Y.setDecimals(4)
        self.OBJ_COORD_Y.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_7.addWidget(self.OBJ_COORD_Y)

        self.OBJ_COORD_Z = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.OBJ_COORD_Z.setObjectName(u"OBJ_COORD_Z")
        self.OBJ_COORD_Z.setDecimals(4)
        self.OBJ_COORD_Z.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_7.addWidget(self.OBJ_COORD_Z)


        self.LeftLayoutOBJ.addLayout(self.horizontalLayout_7)


        self.CoordsInputs.addLayout(self.LeftLayoutOBJ)

        self.line_2 = QFrame(self.verticalLayoutWidget_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.CoordsInputs.addWidget(self.line_2)

        self.LeftLayoutREC = QVBoxLayout()
        self.LeftLayoutREC.setObjectName(u"LeftLayoutREC")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.LeftLayoutREC.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.REC_COORD_X = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.REC_COORD_X.setObjectName(u"REC_COORD_X")
        self.REC_COORD_X.setDecimals(4)
        self.REC_COORD_X.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_3.addWidget(self.REC_COORD_X)

        self.REC_COORD_Y = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.REC_COORD_Y.setObjectName(u"REC_COORD_Y")
        self.REC_COORD_Y.setDecimals(4)
        self.REC_COORD_Y.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_3.addWidget(self.REC_COORD_Y)

        self.REC_COORD_Z = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.REC_COORD_Z.setObjectName(u"REC_COORD_Z")
        self.REC_COORD_Z.setDecimals(4)
        self.REC_COORD_Z.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_3.addWidget(self.REC_COORD_Z)


        self.LeftLayoutREC.addLayout(self.horizontalLayout_3)


        self.CoordsInputs.addLayout(self.LeftLayoutREC)


        self.ObjInputGrid.addLayout(self.CoordsInputs, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_11 = QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QFrame.WinPanel)
        self.label_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.label_11)

        self.label_12 = QLabel(self.verticalLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QFrame.WinPanel)
        self.label_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.label_12)

        self.label_13 = QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setFrameShape(QFrame.WinPanel)
        self.label_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.label_13)


        self.ObjInputGrid.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.line_3 = QFrame(self.verticalLayoutWidget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.ObjInputGrid.addWidget(self.line_3, 0, 3, 1, 1)

        self.line = QFrame(self.verticalLayoutWidget_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.ObjInputGrid.addWidget(self.line, 0, 1, 1, 1)


        self.InputLayout.addLayout(self.ObjInputGrid)

        self.horizontalLayoutWidget_7 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(30, 480, 1031, 51))
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Button = QPushButton(self.horizontalLayoutWidget_7)
        self.Button.setObjectName(u"Button")
        self.Button.setMinimumSize(QSize(240, 40))

        self.horizontalLayout_19.addWidget(self.Button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_2)

        self.Dist_txt = QLabel(self.horizontalLayoutWidget_7)
        self.Dist_txt.setObjectName(u"Dist_txt")
        font1 = QFont()
        font1.setPointSize(16)
        self.Dist_txt.setFont(font1)

        self.horizontalLayout_19.addWidget(self.Dist_txt)

        self.DIST_NUM = QLCDNumber(self.horizontalLayoutWidget_7)
        self.DIST_NUM.setObjectName(u"DIST_NUM")
        self.DIST_NUM.setEnabled(True)
        self.DIST_NUM.setMinimumSize(QSize(180, 0))
        self.DIST_NUM.setProperty("intValue", 0)

        self.horizontalLayout_19.addWidget(self.DIST_NUM)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1103, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Energy:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Direction:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Radius:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Critical Energy:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Coords:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Coords:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Coords:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Radiator:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Object", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Reciever:", None))
        self.Button.setText(QCoreApplication.translate("MainWindow", u"Calculate!", None))
        self.Dist_txt.setText(QCoreApplication.translate("MainWindow", u"Distance:", None))
    # retranslateUi

