# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 556)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.mainBodyTabs = QtWidgets.QStackedWidget(self.centralwidget)
        self.mainBodyTabs.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.mainBodyTabs.sizePolicy().hasHeightForWidth())
        self.mainBodyTabs.setSizePolicy(sizePolicy)
        self.mainBodyTabs.setMinimumSize(QtCore.QSize(0, 0))
        self.mainBodyTabs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainBodyTabs.setStyleSheet("background-color: rgb(255,255,255);\n"
"")
        self.mainBodyTabs.setObjectName("mainBodyTabs")
        self.tablePage = QtWidgets.QWidget()
        self.tablePage.setMinimumSize(QtCore.QSize(600, 0))
        self.tablePage.setStyleSheet("")
        self.tablePage.setObjectName("tablePage")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tablePage)
        self.formLayout_2.setObjectName("formLayout_2")
        self.frame_30 = QtWidgets.QFrame(self.tablePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setMinimumSize(QtCore.QSize(200, 300))
        self.frame_30.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_30.setStyleSheet("background-color:#50A7BC;\n"
"border-radius:10px;")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.studentsFrame = QtWidgets.QFrame(self.frame_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentsFrame.sizePolicy().hasHeightForWidth())
        self.studentsFrame.setSizePolicy(sizePolicy)
        self.studentsFrame.setMinimumSize(QtCore.QSize(170, 40))
        self.studentsFrame.setMaximumSize(QtCore.QSize(200, 40))
        self.studentsFrame.setStyleSheet("border: none;\n"
"\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.studentsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.studentsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.studentsFrame.setObjectName("studentsFrame")
        self.studentsBtn = QtWidgets.QPushButton(self.studentsFrame)
        self.studentsBtn.setGeometry(QtCore.QRect(0, 0, 171, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentsBtn.sizePolicy().hasHeightForWidth())
        self.studentsBtn.setSizePolicy(sizePolicy)
        self.studentsBtn.setMinimumSize(QtCore.QSize(160, 40))
        self.studentsBtn.setMaximumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.studentsBtn.setFont(font)
        self.studentsBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.studentsBtn.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 0, 127);\n"
"    border: none;\n"
"    background-color: rgba(255,255,255);\n"
"    border-radius: 10px\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #001f3f; /* Navy blue border on hover */\n"
"    border-radius: 5px; /* Optional: Add border-radius for a rounded look */\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/student-inactive.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/img/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.studentsBtn.setIcon(icon)
        self.studentsBtn.setIconSize(QtCore.QSize(28, 28))
        self.studentsBtn.setCheckable(True)
        self.studentsBtn.setObjectName("studentsBtn")
        self.verticalLayout.addWidget(self.studentsFrame)
        self.staffFrame = QtWidgets.QFrame(self.frame_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.staffFrame.sizePolicy().hasHeightForWidth())
        self.staffFrame.setSizePolicy(sizePolicy)
        self.staffFrame.setMinimumSize(QtCore.QSize(170, 40))
        self.staffFrame.setMaximumSize(QtCore.QSize(200, 40))
        self.staffFrame.setStyleSheet("border: none;\n"
"\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.staffFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.staffFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.staffFrame.setObjectName("staffFrame")
        self.staffBtn = QtWidgets.QPushButton(self.staffFrame)
        self.staffBtn.setGeometry(QtCore.QRect(0, 0, 171, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.staffBtn.sizePolicy().hasHeightForWidth())
        self.staffBtn.setSizePolicy(sizePolicy)
        self.staffBtn.setMinimumSize(QtCore.QSize(160, 40))
        self.staffBtn.setMaximumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.staffBtn.setFont(font)
        self.staffBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.staffBtn.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 0, 127);\n"
"    border: none;\n"
"    background-color: rgba(255,255,255);\n"
"    border-radius: 10px\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #001f3f; /* Navy blue border on hover */\n"
"    border-radius: 5px; /* Optional: Add border-radius for a rounded look */\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/staff-inactive.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.staffBtn.setIcon(icon1)
        self.staffBtn.setIconSize(QtCore.QSize(32, 32))
        self.staffBtn.setCheckable(True)
        self.staffBtn.setObjectName("staffBtn")
        self.verticalLayout.addWidget(self.staffFrame)
        self.frame_5 = QtWidgets.QFrame(self.frame_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(170, 40))
        self.frame_5.setMaximumSize(QtCore.QSize(200, 40))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 181, 40))
        self.pushButton.setMinimumSize(QtCore.QSize(170, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 40))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 0, 127);\n"
"    border: none;\n"
"    background-color: rgba(255,255,255);\n"
"    border-radius: 10px\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #001f3f; /* Navy blue border on hover */\n"
"    border-radius: 5px; /* Optional: Add border-radius for a rounded look */\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.frame_5)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_30)
        self.frame_2 = QtWidgets.QFrame(self.tablePage)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame_2)
        self.mainBodyTabs.addWidget(self.tablePage)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.formLayout = QtWidgets.QFormLayout(self.page)
        self.formLayout.setObjectName("formLayout")
        self.frame_31 = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy)
        self.frame_31.setMinimumSize(QtCore.QSize(200, 300))
        self.frame_31.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_31.setStyleSheet("background-color:#50A7BC;\n"
"border-radius:10px;")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.studentsFrame_2 = QtWidgets.QFrame(self.frame_31)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentsFrame_2.sizePolicy().hasHeightForWidth())
        self.studentsFrame_2.setSizePolicy(sizePolicy)
        self.studentsFrame_2.setMinimumSize(QtCore.QSize(170, 40))
        self.studentsFrame_2.setMaximumSize(QtCore.QSize(200, 40))
        self.studentsFrame_2.setStyleSheet("border: none;\n"
"\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.studentsFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.studentsFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.studentsFrame_2.setObjectName("studentsFrame_2")
        self.studentsBtn_2 = QtWidgets.QPushButton(self.studentsFrame_2)
        self.studentsBtn_2.setGeometry(QtCore.QRect(0, 0, 171, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentsBtn_2.sizePolicy().hasHeightForWidth())
        self.studentsBtn_2.setSizePolicy(sizePolicy)
        self.studentsBtn_2.setMinimumSize(QtCore.QSize(160, 40))
        self.studentsBtn_2.setMaximumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.studentsBtn_2.setFont(font)
        self.studentsBtn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.studentsBtn_2.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 0, 127);\n"
"    border: none;\n"
"    background-color: rgba(255,255,255);\n"
"    border-radius: 10px\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #001f3f; /* Navy blue border on hover */\n"
"    border-radius: 5px; /* Optional: Add border-radius for a rounded look */\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.studentsBtn_2.setIcon(icon)
        self.studentsBtn_2.setIconSize(QtCore.QSize(28, 28))
        self.studentsBtn_2.setCheckable(True)
        self.studentsBtn_2.setObjectName("studentsBtn_2")
        self.verticalLayout_5.addWidget(self.studentsFrame_2)
        self.staffFrame_2 = QtWidgets.QFrame(self.frame_31)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.staffFrame_2.sizePolicy().hasHeightForWidth())
        self.staffFrame_2.setSizePolicy(sizePolicy)
        self.staffFrame_2.setMinimumSize(QtCore.QSize(170, 40))
        self.staffFrame_2.setMaximumSize(QtCore.QSize(200, 40))
        self.staffFrame_2.setStyleSheet("border: none;\n"
"\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.staffFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.staffFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.staffFrame_2.setObjectName("staffFrame_2")
        self.staffBtn_2 = QtWidgets.QPushButton(self.staffFrame_2)
        self.staffBtn_2.setGeometry(QtCore.QRect(0, 0, 171, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.staffBtn_2.sizePolicy().hasHeightForWidth())
        self.staffBtn_2.setSizePolicy(sizePolicy)
        self.staffBtn_2.setMinimumSize(QtCore.QSize(84, 40))
        self.staffBtn_2.setMaximumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.staffBtn_2.setFont(font)
        self.staffBtn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.staffBtn_2.setStyleSheet("QPushButton {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D0D0D0;\n"
"}")
        self.staffBtn_2.setIcon(icon1)
        self.staffBtn_2.setIconSize(QtCore.QSize(32, 32))
        self.staffBtn_2.setCheckable(True)
        self.staffBtn_2.setObjectName("staffBtn_2")
        self.verticalLayout_5.addWidget(self.staffFrame_2)
        self.frame_6 = QtWidgets.QFrame(self.frame_31)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(170, 40))
        self.frame_6.setMaximumSize(QtCore.QSize(200, 40))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 181, 40))
        self.pushButton_2.setMinimumSize(QtCore.QSize(170, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 40))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 0, 127);\n"
"    border: none;\n"
"    background-color: rgba(255,255,255);\n"
"    border-radius: 10px\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #001f3f; /* Navy blue border on hover */\n"
"    border-radius: 5px; /* Optional: Add border-radius for a rounded look */\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.frame_6)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_31)
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.frame_3)
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget_5.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget_5.addTab(self.tab_12, "")
        self.verticalLayout_7.addWidget(self.tabWidget_5)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame_3)
        self.mainBodyTabs.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.page_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.frame_32 = QtWidgets.QFrame(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy)
        self.frame_32.setMinimumSize(QtCore.QSize(200, 300))
        self.frame_32.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_32.setStyleSheet("background-color:#50A7BC;\n"
"border-radius:10px;")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.studentsFrame_3 = QtWidgets.QFrame(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentsFrame_3.sizePolicy().hasHeightForWidth())
        self.studentsFrame_3.setSizePolicy(sizePolicy)
        self.studentsFrame_3.setMinimumSize(QtCore.QSize(170, 40))
        self.studentsFrame_3.setMaximumSize(QtCore.QSize(200, 40))
        self.studentsFrame_3.setStyleSheet("border: none;\n"
"\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.studentsFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.studentsFrame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.studentsFrame_3.setObjectName("studentsFrame_3")
        self.studentsBtn_3 = QtWidgets.QPushButton(self.studentsFrame_3)
        self.studentsBtn_3.setGeometry(QtCore.QRect(0, 0, 171, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentsBtn_3.sizePolicy().hasHeightForWidth())
        self.studentsBtn_3.setSizePolicy(sizePolicy)
        self.studentsBtn_3.setMinimumSize(QtCore.QSize(160, 40))
        self.studentsBtn_3.setMaximumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.studentsBtn_3.setFont(font)
        self.studentsBtn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.studentsBtn_3.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 0, 127);\n"
"    border: none;\n"
"    background-color: rgba(255,255,255);\n"
"    border-radius: 10px\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #001f3f; /* Navy blue border on hover */\n"
"    border-radius: 5px; /* Optional: Add border-radius for a rounded look */\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.studentsBtn_3.setIcon(icon)
        self.studentsBtn_3.setIconSize(QtCore.QSize(28, 28))
        self.studentsBtn_3.setCheckable(True)
        self.studentsBtn_3.setObjectName("studentsBtn_3")
        self.verticalLayout_8.addWidget(self.studentsFrame_3)
        self.staffFrame_3 = QtWidgets.QFrame(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.staffFrame_3.sizePolicy().hasHeightForWidth())
        self.staffFrame_3.setSizePolicy(sizePolicy)
        self.staffFrame_3.setMinimumSize(QtCore.QSize(170, 40))
        self.staffFrame_3.setMaximumSize(QtCore.QSize(200, 40))
        self.staffFrame_3.setStyleSheet("border: none;\n"
"\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.staffFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.staffFrame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.staffFrame_3.setObjectName("staffFrame_3")
        self.staffBtn_3 = QtWidgets.QPushButton(self.staffFrame_3)
        self.staffBtn_3.setGeometry(QtCore.QRect(0, 0, 171, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.staffBtn_3.sizePolicy().hasHeightForWidth())
        self.staffBtn_3.setSizePolicy(sizePolicy)
        self.staffBtn_3.setMinimumSize(QtCore.QSize(160, 40))
        self.staffBtn_3.setMaximumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.staffBtn_3.setFont(font)
        self.staffBtn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.staffBtn_3.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 0, 127);\n"
"    border: none;\n"
"    background-color: rgba(255,255,255);\n"
"    border-radius: 10px\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #001f3f; /* Navy blue border on hover */\n"
"    border-radius: 5px; /* Optional: Add border-radius for a rounded look */\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.staffBtn_3.setIcon(icon1)
        self.staffBtn_3.setIconSize(QtCore.QSize(32, 32))
        self.staffBtn_3.setCheckable(True)
        self.staffBtn_3.setObjectName("staffBtn_3")
        self.verticalLayout_8.addWidget(self.staffFrame_3)
        self.frame_7 = QtWidgets.QFrame(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(170, 40))
        self.frame_7.setMaximumSize(QtCore.QSize(200, 40))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 0, 181, 40))
        self.pushButton_3.setMinimumSize(QtCore.QSize(170, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 40))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 0, 127);\n"
"    border: none;\n"
"    background-color: rgba(255,255,255);\n"
"    border-radius: 10px\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #001f3f; /* Navy blue border on hover */\n"
"    border-radius: 5px; /* Optional: Add border-radius for a rounded look */\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_8.addWidget(self.frame_7)
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_32)
        self.frame_4 = QtWidgets.QFrame(self.page_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tabWidget_7 = QtWidgets.QTabWidget(self.frame_4)
        self.tabWidget_7.setStyleSheet("selection-color: rgb(85, 170, 255);")
        self.tabWidget_7.setObjectName("tabWidget_7")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tabWidget_7.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.tabWidget_7.addTab(self.tab_16, "")
        self.verticalLayout_10.addWidget(self.tabWidget_7)
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame_4)
        self.mainBodyTabs.addWidget(self.page_2)
        self.toolsPage = QtWidgets.QWidget()
        self.toolsPage.setStyleSheet("border:none;")
        self.toolsPage.setObjectName("toolsPage")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.toolsPage)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.mainBodyTabs.addWidget(self.toolsPage)
        self.verticalLayout_4.addWidget(self.mainBodyTabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainBodyTabs.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_5.setCurrentIndex(1)
        self.tabWidget_7.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.studentsBtn.setText(_translate("MainWindow", "     Students"))
        self.staffBtn.setText(_translate("MainWindow", "     Staff"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Add Student"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Show Student Profile"))
        self.studentsBtn_2.setText(_translate("MainWindow", "     Students"))
        self.staffBtn_2.setText(_translate("MainWindow", "     Staff"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_11), _translate("MainWindow", "Add Professor"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_12), _translate("MainWindow", "Show Professor Profile"))
        self.studentsBtn_3.setText(_translate("MainWindow", "     Students"))
        self.staffBtn_3.setText(_translate("MainWindow", "Proffesor"))
        self.pushButton_3.setText(_translate("MainWindow", "Class"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_15), _translate("MainWindow", "Add Student to Class"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_16), _translate("MainWindow", "Add Professor to Class"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())