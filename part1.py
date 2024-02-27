from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(1004, 711)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
            self.gridLayout_6.setObjectName("gridLayout_6")
            self.frame = QtWidgets.QFrame(self.centralwidget)
            self.frame.setEnabled(True)
            self.frame.setStyleSheet("background-color: rgb(56, 56, 56);\n"
    "")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.gridLayout_11 = QtWidgets.QGridLayout(self.frame)
            self.gridLayout_11.setObjectName("gridLayout_11")
            self.frame_3 = QtWidgets.QFrame(self.frame)
            self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_3.setObjectName("frame_3")
            self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_3)
            self.horizontalLayout_7.setObjectName("horizontalLayout_7")
            self.gridLayout_11.addWidget(self.frame_3, 0, 0, 1, 1)
            self.pushButton = QtWidgets.QPushButton(self.frame)
            self.pushButton.setStyleSheet("QPushButton {\n"
    "    border: 2px solid rgb(51,51,51);\n"
    "    border-radius: 5px;    \n"
    "    color:rgb(255,255,255);\n"
    "    \n"
    "    background-color: rgb(170, 0, 0);\n"
    "padding:9px\n"
    "\n"
    "}\n"
    "QPushButton:hover {\n"
    "    \n"
    "    \n"
    "    background-color: rgb(255, 0, 0);\n"
    "}\n"
    "QPushButton:pressed {    \n"
    "    border: 2px solid rgb(0,143,150);\n"
    "    background-color: rgb(51,51,51);\n"
    "}\n"
    "\n"
    "QPushButton:disabled {    \n"
    "    border-radius: 5px;    \n"
    "    border: 2px solid rgb(112,112,112);\n"
    "    background-color: rgb(112,112,112);\n"
    "}")
            self.pushButton.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/closeAsset 43.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton.setIcon(icon)
            self.pushButton.setObjectName("pushButton")
            self.gridLayout_11.addWidget(self.pushButton, 0, 1, 1, 1)
            self.frame_6 = QtWidgets.QFrame(self.frame)
            self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_6.setObjectName("frame_6")
            self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_6)
            self.gridLayout_10.setObjectName("gridLayout_10")
            self.mainBodyTabs = QtWidgets.QStackedWidget(self.frame_6)
            self.mainBodyTabs.setEnabled(True)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(200)
            sizePolicy.setVerticalStretch(200)
            sizePolicy.setHeightForWidth(self.mainBodyTabs.sizePolicy().hasHeightForWidth())
            self.mainBodyTabs.setSizePolicy(sizePolicy)
            self.mainBodyTabs.setMinimumSize(QtCore.QSize(0, 0))
            self.mainBodyTabs.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.mainBodyTabs.setStyleSheet("border-color: rgb(91,90,90);\n"
    "background:rgb(91,90,90);\n"
    "selection-color: rgb(0, 0, 0);")
            self.mainBodyTabs.setObjectName("mainBodyTabs")
            self.page_4 = QtWidgets.QWidget()
            self.page_4.setObjectName("page_4")
            self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_4)
            self.verticalLayout_3.setObjectName("verticalLayout_3")
            self.frame_2 = QtWidgets.QFrame(self.page_4)
            self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_2.setObjectName("frame_2")
            self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
            self.gridLayout_3.setObjectName("gridLayout_3")
            self.graphicsView_1 = QtWidgets.QGraphicsView(self.frame_2)
            self.graphicsView_1.setObjectName("graphicsView_1")
            self.gridLayout_3.addWidget(self.graphicsView_1, 1, 0, 1, 1)
            self.verticalLayout_3.addWidget(self.frame_2)
            self.mainBodyTabs.addWidget(self.page_4)
            self.page_staff = QtWidgets.QWidget()
            self.page_staff.setObjectName("page_staff")
            self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_staff)
            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
            self.frame_staff = QtWidgets.QFrame(self.page_staff)
            self.frame_staff.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_staff.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_staff.setObjectName("frame_staff")
            self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_staff)
            self.verticalLayout_7.setObjectName("verticalLayout_7")
            self.Prof_Tab = QtWidgets.QTabWidget(self.frame_staff)
            self.Prof_Tab.setIconSize(QtCore.QSize(12, 12))
            self.Prof_Tab.setObjectName("Prof_Tab")
            self.Add_Prof_Tab = QtWidgets.QWidget()
            self.Add_Prof_Tab.setObjectName("Add_Prof_Tab")
            self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.Add_Prof_Tab)
            self.verticalLayout_17.setObjectName("verticalLayout_17")
            self.gridLayout_4 = QtWidgets.QGridLayout()
            self.gridLayout_4.setObjectName("gridLayout_4")
            self.frame_25 = QtWidgets.QFrame(self.Add_Prof_Tab)
            self.frame_25.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_25.setObjectName("frame_25")
            self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_25)
            self.verticalLayout_13.setObjectName("verticalLayout_13")
            self.Prof_LName_LineEdit = QtWidgets.QLineEdit(self.frame_25)
            self.Prof_LName_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
            self.Prof_LName_LineEdit.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Prof_LName_LineEdit.setObjectName("Prof_LName_LineEdit")
            self.verticalLayout_13.addWidget(self.Prof_LName_LineEdit)
            self.gridLayout_4.addWidget(self.frame_25, 0, 3, 1, 1)
            self.frame_26 = QtWidgets.QFrame(self.Add_Prof_Tab)
            self.frame_26.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_26.setObjectName("frame_26")
            self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_26)
            self.horizontalLayout_15.setObjectName("horizontalLayout_15")
            self.label_20 = QtWidgets.QLabel(self.frame_26)
            self.label_20.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_20.setObjectName("label_20")
            self.horizontalLayout_15.addWidget(self.label_20)
            self.Prof_Mobile_LineEdit = QtWidgets.QLineEdit(self.frame_26)
            self.Prof_Mobile_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
            self.Prof_Mobile_LineEdit.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Prof_Mobile_LineEdit.setObjectName("Prof_Mobile_LineEdit")
            self.horizontalLayout_15.addWidget(self.Prof_Mobile_LineEdit)
            self.gridLayout_4.addWidget(self.frame_26, 1, 2, 1, 2)
            self.frame_27 = QtWidgets.QFrame(self.Add_Prof_Tab)
            self.frame_27.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_27.setObjectName("frame_27")
            self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_27)
            self.horizontalLayout_16.setObjectName("horizontalLayout_16")
            self.label_21 = QtWidgets.QLabel(self.frame_27)
            self.label_21.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_21.setObjectName("label_21")
            self.horizontalLayout_16.addWidget(self.label_21)
            self.Prof_Title_LineEdit = QtWidgets.QLineEdit(self.frame_27)
            self.Prof_Title_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
            self.Prof_Title_LineEdit.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Prof_Title_LineEdit.setObjectName("Prof_Title_LineEdit")
            self.horizontalLayout_16.addWidget(self.Prof_Title_LineEdit)
            self.gridLayout_4.addWidget(self.frame_27, 3, 2, 1, 1)
            self.frame_28 = QtWidgets.QFrame(self.Add_Prof_Tab)
            self.frame_28.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_28.setObjectName("frame_28")
            self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_28)
            self.horizontalLayout_17.setObjectName("horizontalLayout_17")
            self.label_22 = QtWidgets.QLabel(self.frame_28)
            self.label_22.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_22.setObjectName("label_22")
            self.horizontalLayout_17.addWidget(self.label_22)
            self.Prof_Age_SpinBox = QtWidgets.QSpinBox(self.frame_28)
            self.Prof_Age_SpinBox.setMinimumSize(QtCore.QSize(100, 26))
            self.Prof_Age_SpinBox.setStyleSheet("QSpinBox {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QSpinBox:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QSpinBox:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "\n"
    "QSpinBox::up-button {\n"
    "    subcontrol-origin: border;\n"
    "    subcontrol-position: top right;\n"
    "    border: 2px solid rgb(74, 148, 146); \n"
    "    width: 16px; /* Adjust button width */\n"
    "    \n"
    "}\n"
    "\n"
    "QSpinBox::down-button {\n"
    "    subcontrol-origin: border;\n"
    "    subcontrol-position: bottom right;\n"
    "    width: 16px; /* Adjust button width */\n"
    "    border: 2px solid rgb(74, 148, 146); \n"
    "    \n"
    "}\n"
    "\n"
    "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
    "    background-color: rgba(255, 255, 255, 0.1); \n"
    "border: 2px solid rgb(0, 255, 255);\n"
    "\n"
    "}\n"
    "QSpinBox::up-button:focus, QSpinBox::down-button:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "")
            self.Prof_Age_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
            self.Prof_Age_SpinBox.setObjectName("Prof_Age_SpinBox")
            self.horizontalLayout_17.addWidget(self.Prof_Age_SpinBox)
            self.gridLayout_4.addWidget(self.frame_28, 3, 3, 1, 1)
            self.frame_29 = QtWidgets.QFrame(self.Add_Prof_Tab)
            self.frame_29.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_29.setObjectName("frame_29")
            self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_29)
            self.horizontalLayout_18.setObjectName("horizontalLayout_18")
            self.label_23 = QtWidgets.QLabel(self.frame_29)
            self.label_23.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_23.setObjectName("label_23")
            self.horizontalLayout_18.addWidget(self.label_23)
            self.Prof_Email_LineEdit = QtWidgets.QLineEdit(self.frame_29)
            self.Prof_Email_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
            self.Prof_Email_LineEdit.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Prof_Email_LineEdit.setObjectName("Prof_Email_LineEdit")
            self.horizontalLayout_18.addWidget(self.Prof_Email_LineEdit)
            self.gridLayout_4.addWidget(self.frame_29, 2, 2, 1, 2)
            self.prof_name = QtWidgets.QFrame(self.Add_Prof_Tab)
            self.prof_name.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.prof_name.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.prof_name.setFrameShadow(QtWidgets.QFrame.Raised)
            self.prof_name.setObjectName("prof_name")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.prof_name)
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.profName_lab = QtWidgets.QLabel(self.prof_name)
            self.profName_lab.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.profName_lab.setObjectName("profName_lab")
            self.horizontalLayout.addWidget(self.profName_lab)
            self.Prof_FName_LineEdit = QtWidgets.QLineEdit(self.prof_name)
            self.Prof_FName_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
            self.Prof_FName_LineEdit.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Prof_FName_LineEdit.setObjectName("Prof_FName_LineEdit")
            self.horizontalLayout.addWidget(self.Prof_FName_LineEdit)
            self.gridLayout_4.addWidget(self.prof_name, 0, 2, 1, 1)
            self.verticalLayout_17.addLayout(self.gridLayout_4)
            self.Prof_Add_Btn = QtWidgets.QPushButton(self.Add_Prof_Tab)
            self.Prof_Add_Btn.setStyleSheet("QPushButton {\n"
    "    border: 2px solid rgb(51,51,51);\n"
    "    border-radius: 5px;    \n"
    "    color:rgb(255,255,255);\n"
    "    background-color: rgb(51,51,51);\n"
    "    background-color: rgb(0,143,150);\n"
    "\n"
    "}\n"
    "QPushButton:hover {\n"
    "    \n"
    "    background-color: rgb(0, 255, 255);\n"
    "}\n"
    "QPushButton:pressed {    \n"
    "    border: 2px solid rgb(0,143,150);\n"
    "    background-color: rgb(51,51,51);\n"
    "}\n"
    "\n"
    "QPushButton:disabled {    \n"
    "    border-radius: 5px;    \n"
    "    border: 2px solid rgb(112,112,112);\n"
    "    background-color: rgb(112,112,112);\n"
    "}")
            self.Prof_Add_Btn.setObjectName("Prof_Add_Btn")
            self.verticalLayout_17.addWidget(self.Prof_Add_Btn)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icons/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Prof_Tab.addTab(self.Add_Prof_Tab, icon1, "")
            self.Search_Prof_Tab = QtWidgets.QWidget()
            self.Search_Prof_Tab.setObjectName("Search_Prof_Tab")
            self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Search_Prof_Tab)
            self.verticalLayout_5.setObjectName("verticalLayout_5")
            self.frame_12 = QtWidgets.QFrame(self.Search_Prof_Tab)
            self.frame_12.setEnabled(True)
            self.frame_12.setMaximumSize(QtCore.QSize(16777215, 80))
            self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_12.setObjectName("frame_12")
            self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_12)
            self.horizontalLayout_31.setObjectName("horizontalLayout_31")
            self.Prof_SearchBar = QtWidgets.QLineEdit(self.frame_12)
            self.Prof_SearchBar.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Prof_SearchBar.setObjectName("Prof_SearchBar")
            self.horizontalLayout_31.addWidget(self.Prof_SearchBar)
            self.Student_Search_Btn_2 = QtWidgets.QPushButton(self.frame_12)
            self.Student_Search_Btn_2.setStyleSheet("QPushButton {\n"
    "    border: 2px solid rgb(51,51,51);\n"
    "    border-radius: 5px;    \n"
    "    color:rgb(255,255,255);\n"
    "    background-color: rgb(51,51,51);\n"
    "    background-color: rgb(0,143,150);\n"
    "padding:9px\n"
    "\n"
    "}\n"
    "QPushButton:hover {\n"
    "    \n"
    "    background-color: rgb(0, 255, 255);\n"
    "}\n"
    "QPushButton:pressed {    \n"
    "    border: 2px solid rgb(0,143,150);\n"
    "    background-color: rgb(51,51,51);\n"
    "}\n"
    "\n"
    "QPushButton:disabled {    \n"
    "    border-radius: 5px;    \n"
    "    border: 2px solid rgb(112,112,112);\n"
    "    background-color: rgb(112,112,112);\n"
    "}")
            self.Student_Search_Btn_2.setText("")
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(":/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Student_Search_Btn_2.setIcon(icon2)
            self.Student_Search_Btn_2.setObjectName("Student_Search_Btn_2")
            self.horizontalLayout_31.addWidget(self.Student_Search_Btn_2)
            self.verticalLayout_5.addWidget(self.frame_12)
            self.frame_13 = QtWidgets.QFrame(self.Search_Prof_Tab)
            self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_13.setObjectName("frame_13")
            self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_13)
            self.gridLayout_5.setObjectName("gridLayout_5")
            self.gridLayout_12 = QtWidgets.QGridLayout()
            self.gridLayout_12.setObjectName("gridLayout_12")
            self.frame_54 = QtWidgets.QFrame(self.frame_13)
            self.frame_54.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_54.setObjectName("frame_54")
            self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_54)
            self.horizontalLayout_20.setObjectName("horizontalLayout_20")
            self.label_40 = QtWidgets.QLabel(self.frame_54)
            self.label_40.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_40.setObjectName("label_40")
            self.horizontalLayout_20.addWidget(self.label_40)
            self.label_17 = QtWidgets.QLabel(self.frame_54)
            self.label_17.setMinimumSize(QtCore.QSize(200, 0))
            self.label_17.setMaximumSize(QtCore.QSize(300, 40))
            self.label_17.setStyleSheet("QLabel {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QLabel:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QLabel:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "")
            self.label_17.setObjectName("label_17")
            self.horizontalLayout_20.addWidget(self.label_17)
            self.gridLayout_12.addWidget(self.frame_54, 0, 2, 1, 1)
            self.frame_55 = QtWidgets.QFrame(self.frame_13)
            self.frame_55.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_55.setObjectName("frame_55")
            self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_55)
            self.horizontalLayout_21.setObjectName("horizontalLayout_21")
            self.label_41 = QtWidgets.QLabel(self.frame_55)
            self.label_41.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_41.setObjectName("label_41")
            self.horizontalLayout_21.addWidget(self.label_41)
            self.label_18 = QtWidgets.QLabel(self.frame_55)
            self.label_18.setMinimumSize(QtCore.QSize(200, 0))
            self.label_18.setMaximumSize(QtCore.QSize(300, 40))
            self.label_18.setStyleSheet("QLabel {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QLabel:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QLabel:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "")
            self.label_18.setObjectName("label_18")
            self.horizontalLayout_21.addWidget(self.label_18)
            self.gridLayout_12.addWidget(self.frame_55, 3, 3, 1, 1)
            self.frame_56 = QtWidgets.QFrame(self.frame_13)
            self.frame_56.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_56.setObjectName("frame_56")
            self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_56)
            self.horizontalLayout_22.setObjectName("horizontalLayout_22")
            self.label_42 = QtWidgets.QLabel(self.frame_56)
            self.label_42.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_42.setObjectName("label_42")
            self.horizontalLayout_22.addWidget(self.label_42)
            self.label_19 = QtWidgets.QLabel(self.frame_56)
            self.label_19.setMinimumSize(QtCore.QSize(480, 0))
            self.label_19.setMaximumSize(QtCore.QSize(300, 40))
            self.label_19.setStyleSheet("QLabel {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QLabel:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QLabel:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "")
            self.label_19.setObjectName("label_19")
            self.horizontalLayout_22.addWidget(self.label_19)
            self.gridLayout_12.addWidget(self.frame_56, 2, 2, 1, 2)
            self.frame_57 = QtWidgets.QFrame(self.frame_13)
            self.frame_57.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_57.setObjectName("frame_57")
            self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_57)
            self.horizontalLayout_27.setObjectName("horizontalLayout_27")
            self.label_43 = QtWidgets.QLabel(self.frame_57)
            self.label_43.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_43.setObjectName("label_43")
            self.horizontalLayout_27.addWidget(self.label_43)
            self.label_24 = QtWidgets.QLabel(self.frame_57)
            self.label_24.setMinimumSize(QtCore.QSize(200, 0))
            self.label_24.setMaximumSize(QtCore.QSize(300, 40))
            self.label_24.setStyleSheet("QLabel {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QLabel:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QLabel:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "")
            self.label_24.setObjectName("label_24")
            self.horizontalLayout_27.addWidget(self.label_24)
            self.gridLayout_12.addWidget(self.frame_57, 3, 2, 1, 1)
            self.frame_58 = QtWidgets.QFrame(self.frame_13)
            self.frame_58.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_58.setObjectName("frame_58")
            self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_58)
            self.horizontalLayout_28.setObjectName("horizontalLayout_28")
            self.label_25 = QtWidgets.QLabel(self.frame_58)
            self.label_25.setMinimumSize(QtCore.QSize(200, 0))
            self.label_25.setMaximumSize(QtCore.QSize(300, 40))
            self.label_25.setStyleSheet("QLabel {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QLabel:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QLabel:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "")
            self.label_25.setObjectName("label_25")
            self.horizontalLayout_28.addWidget(self.label_25)
            self.gridLayout_12.addWidget(self.frame_58, 0, 3, 1, 1)
            self.frame_59 = QtWidgets.QFrame(self.frame_13)
            self.frame_59.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_59.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_59.setObjectName("frame_59")
            self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_59)
            self.horizontalLayout_29.setObjectName("horizontalLayout_29")
            self.label_44 = QtWidgets.QLabel(self.frame_59)
            self.label_44.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_44.setObjectName("label_44")
            self.horizontalLayout_29.addWidget(self.label_44)
            self.label_26 = QtWidgets.QLabel(self.frame_59)
            self.label_26.setMinimumSize(QtCore.QSize(480, 0))
            self.label_26.setMaximumSize(QtCore.QSize(300, 40))
            self.label_26.setStyleSheet("QLabel {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QLabel:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QLabel:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "")
            self.label_26.setObjectName("label_26")
            self.horizontalLayout_29.addWidget(self.label_26)
            self.gridLayout_12.addWidget(self.frame_59, 1, 2, 1, 2)
            self.gridLayout_5.addLayout(self.gridLayout_12, 0, 0, 1, 1)
            self.verticalLayout_5.addWidget(self.frame_13)
            self.Prof_Tab.addTab(self.Search_Prof_Tab, icon2, "")
            self.verticalLayout_7.addWidget(self.Prof_Tab)
            self.horizontalLayout_5.addWidget(self.frame_staff)
            self.mainBodyTabs.addWidget(self.page_staff)
            self.page_2 = QtWidgets.QWidget()
            self.page_2.setObjectName("page_2")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_2)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.Class_Search_Bar3_Btn = QtWidgets.QTabWidget(self.page_2)
            self.Class_Search_Bar3_Btn.setStyleSheet("")
            self.Class_Search_Bar3_Btn.setIconSize(QtCore.QSize(12, 12))
            self.Class_Search_Bar3_Btn.setObjectName("Class_Search_Bar3_Btn")
            self.Add_Prof_Class_Tab = QtWidgets.QWidget()
            self.Add_Prof_Class_Tab.setObjectName("Add_Prof_Class_Tab")
            self.gridLayout = QtWidgets.QGridLayout(self.Add_Prof_Class_Tab)
            self.gridLayout.setObjectName("gridLayout")
            self.Prof_Search_Bar2 = QtWidgets.QLineEdit(self.Add_Prof_Class_Tab)
            self.Prof_Search_Bar2.setWhatsThis("")
            self.Prof_Search_Bar2.setAccessibleDescription("")
            self.Prof_Search_Bar2.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Prof_Search_Bar2.setObjectName("Prof_Search_Bar2")
            self.gridLayout.addWidget(self.Prof_Search_Bar2, 0, 0, 1, 1)
            self.Class_Search_Bar2 = QtWidgets.QLineEdit(self.Add_Prof_Class_Tab)
            self.Class_Search_Bar2.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Class_Search_Bar2.setObjectName("Class_Search_Bar2")
            self.gridLayout.addWidget(self.Class_Search_Bar2, 1, 0, 1, 1)
            self.Add_Prof_Class_Btn = QtWidgets.QPushButton(self.Add_Prof_Class_Tab)
            self.Add_Prof_Class_Btn.setStyleSheet("QPushButton {\n"
    "    border: 2px solid rgb(51,51,51);\n"
    "    border-radius: 5px;    \n"
    "    color:rgb(255,255,255);\n"
    "    background-color: rgb(51,51,51);\n"
    "    background-color: rgb(0,143,150);\n"
    "\n"
    "}\n"
    "QPushButton:hover {\n"
    "    \n"
    "    background-color: rgb(0, 255, 255);\n"
    "}\n"
    "QPushButton:pressed {    \n"
    "    border: 2px solid rgb(0,143,150);\n"
    "    background-color: rgb(51,51,51);\n"
    "}\n"
    "\n"
    "QPushButton:disabled {    \n"
    "    border-radius: 5px;    \n"
    "    border: 2px solid rgb(112,112,112);\n"
    "    background-color: rgb(112,112,112);\n"
    "}")
            self.Add_Prof_Class_Btn.setObjectName("Add_Prof_Class_Btn")
            self.gridLayout.addWidget(self.Add_Prof_Class_Btn, 2, 0, 1, 1)
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap(":/icons/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Class_Search_Bar3_Btn.addTab(self.Add_Prof_Class_Tab, icon3, "")
            self.Add_Student_Class_Tab = QtWidgets.QWidget()
            self.Add_Student_Class_Tab.setObjectName("Add_Student_Class_Tab")
            self.gridLayout_2 = QtWidgets.QGridLayout(self.Add_Student_Class_Tab)
            self.gridLayout_2.setObjectName("gridLayout_2")
            self.Add_Student_Class_Btn = QtWidgets.QPushButton(self.Add_Student_Class_Tab)
            self.Add_Student_Class_Btn.setStyleSheet("QPushButton {\n"
    "    border: 2px solid rgb(51,51,51);\n"
    "    border-radius: 5px;    \n"
    "    color:rgb(255,255,255);\n"
    "    background-color: rgb(51,51,51);\n"
    "    background-color: rgb(0,143,150);\n"
    "\n"
    "}\n"
    "QPushButton:hover {\n"
    "    \n"
    "    background-color: rgb(0, 255, 255);\n"
    "}\n"
    "QPushButton:pressed {    \n"
    "    border: 2px solid rgb(0,143,150);\n"
    "    background-color: rgb(51,51,51);\n"
    "}\n"
    "\n"
    "QPushButton:disabled {    \n"
    "    border-radius: 5px;    \n"
    "    border: 2px solid rgb(112,112,112);\n"
    "    background-color: rgb(112,112,112);\n"
    "}")
            self.Add_Student_Class_Btn.setObjectName("Add_Student_Class_Btn")
            self.gridLayout_2.addWidget(self.Add_Student_Class_Btn, 2, 0, 1, 1)
            self.Class_Search_Bar3 = QtWidgets.QLineEdit(self.Add_Student_Class_Tab)
            self.Class_Search_Bar3.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Class_Search_Bar3.setObjectName("Class_Search_Bar3")
            self.gridLayout_2.addWidget(self.Class_Search_Bar3, 1, 0, 1, 1)
            self.Student_Search_Bar2 = QtWidgets.QLineEdit(self.Add_Student_Class_Tab)
            self.Student_Search_Bar2.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Student_Search_Bar2.setObjectName("Student_Search_Bar2")
            self.gridLayout_2.addWidget(self.Student_Search_Bar2, 0, 0, 1, 1)
            self.Class_Search_Bar3_Btn.addTab(self.Add_Student_Class_Tab, icon3, "")
            self.Sarch_Class_Tab = QtWidgets.QWidget()
            self.Sarch_Class_Tab.setObjectName("Sarch_Class_Tab")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Sarch_Class_Tab)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.frame_7 = QtWidgets.QFrame(self.Sarch_Class_Tab)
            self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_7.setObjectName("frame_7")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.Class_SearchBar = QtWidgets.QLineEdit(self.frame_7)
            self.Class_SearchBar.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Class_SearchBar.setObjectName("Class_SearchBar")
            self.horizontalLayout_2.addWidget(self.Class_SearchBar)
            self.Student_Search_Btn_7 = QtWidgets.QPushButton(self.frame_7)
            self.Student_Search_Btn_7.setStyleSheet("QPushButton {\n"
    "    border: 2px solid rgb(51,51,51);\n"
    "    border-radius: 5px;    \n"
    "    color:rgb(255,255,255);\n"
    "    background-color: rgb(51,51,51);\n"
    "    background-color: rgb(0,143,150);\n"
    "padding:9px\n"
    "\n"
    "}\n"
    "QPushButton:hover {\n"
    "    \n"
    "    background-color: rgb(0, 255, 255);\n"
    "}\n"
    "QPushButton:pressed {    \n"
    "    border: 2px solid rgb(0,143,150);\n"
    "    background-color: rgb(51,51,51);\n"
    "}\n"
    "\n"
    "QPushButton:disabled {    \n"
    "    border-radius: 5px;    \n"
    "    border: 2px solid rgb(112,112,112);\n"
    "    background-color: rgb(112,112,112);\n"
    "}")
            self.Student_Search_Btn_7.setText("")
            self.Student_Search_Btn_7.setIcon(icon2)
            self.Student_Search_Btn_7.setObjectName("Student_Search_Btn_7")
            self.horizontalLayout_2.addWidget(self.Student_Search_Btn_7)
            self.verticalLayout_2.addWidget(self.frame_7)
            self.frame_20 = QtWidgets.QFrame(self.Sarch_Class_Tab)
            self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_20.setObjectName("frame_20")
            self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.frame_20)
            self.horizontalLayout_36.setObjectName("horizontalLayout_36")
            self.class_info_TW = QtWidgets.QTableWidget(self.frame_20)
            self.class_info_TW.setObjectName("class_info_TW")
            self.class_info_TW.setColumnCount(0)
            self.class_info_TW.setRowCount(0)
            self.horizontalLayout_36.addWidget(self.class_info_TW)
            self.professor_TW = QtWidgets.QTableWidget(self.frame_20)
            self.professor_TW.setObjectName("professor_TW")
            self.professor_TW.setColumnCount(0)
            self.professor_TW.setRowCount(0)
            from PyQt5.QtWidgets import QSizePolicy

            self.horizontalLayout_36.addWidget(self.professor_TW)
            self.verticalLayout_2.addWidget(self.frame_20)
            self.class_search_result = QtWidgets.QTableWidget(self.Sarch_Class_Tab)
            self.class_search_result.setObjectName("class_search_result")
            self.class_search_result.setColumnCount(0)
            self.class_search_result.setRowCount(0)
            self.verticalLayout_2.addWidget(self.class_search_result)
            self.class_search_result.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.Class_Search_Bar3_Btn.addTab(self.Sarch_Class_Tab, icon2, "")
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName("tab")
            self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab)
            self.horizontalLayout_8.setObjectName("horizontalLayout_8")
            self.frame_15 = QtWidgets.QFrame(self.tab)
            self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_15.setObjectName("frame_15")
            self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_15)
            self.verticalLayout_8.setObjectName("verticalLayout_8")
            self.frame_16 = QtWidgets.QFrame(self.frame_15)
            self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_16.setObjectName("frame_16")
            self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_16)
            self.horizontalLayout_32.setObjectName("horizontalLayout_32")
            self.label_27 = QtWidgets.QLabel(self.frame_16)
            self.label_27.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_27.setObjectName("label_27")
            self.horizontalLayout_32.addWidget(self.label_27)
            self.Student_Search_Bar2_2 = QtWidgets.QLineEdit(self.frame_16)
            self.Student_Search_Bar2_2.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Student_Search_Bar2_2.setPlaceholderText("")
            self.Student_Search_Bar2_2.setObjectName("Student_Search_Bar2_2")
            self.horizontalLayout_32.addWidget(self.Student_Search_Bar2_2)
            self.verticalLayout_8.addWidget(self.frame_16)
            self.frame_17 = QtWidgets.QFrame(self.frame_15)
            self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_17.setObjectName("frame_17")
            self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_17)
            self.horizontalLayout_33.setObjectName("horizontalLayout_33")
            self.label_28 = QtWidgets.QLabel(self.frame_17)
            self.label_28.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_28.setObjectName("label_28")
            self.horizontalLayout_33.addWidget(self.label_28)
            self.Student_Search_Bar2_3 = QtWidgets.QLineEdit(self.frame_17)
            self.Student_Search_Bar2_3.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Student_Search_Bar2_3.setPlaceholderText("")
            self.Student_Search_Bar2_3.setObjectName("Student_Search_Bar2_3")
            self.horizontalLayout_33.addWidget(self.Student_Search_Bar2_3)
            self.verticalLayout_8.addWidget(self.frame_17)
            self.frame_18 = QtWidgets.QFrame(self.frame_15)
            self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_18.setObjectName("frame_18")
            self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_18)
            self.horizontalLayout_34.setObjectName("horizontalLayout_34")
            self.label_29 = QtWidgets.QLabel(self.frame_18)
            self.label_29.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_29.setObjectName("label_29")
            self.horizontalLayout_34.addWidget(self.label_29)
            self.Student_Search_Bar2_5 = QtWidgets.QLineEdit(self.frame_18)
            self.Student_Search_Bar2_5.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Student_Search_Bar2_5.setPlaceholderText("")
            self.Student_Search_Bar2_5.setObjectName("Student_Search_Bar2_5")
            self.horizontalLayout_34.addWidget(self.Student_Search_Bar2_5)
            self.verticalLayout_8.addWidget(self.frame_18)
            self.frame_19 = QtWidgets.QFrame(self.frame_15)
            self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_19.setObjectName("frame_19")
            self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_19)
            self.horizontalLayout_35.setObjectName("horizontalLayout_35")
            self.label_45 = QtWidgets.QLabel(self.frame_19)
            self.label_45.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_45.setObjectName("label_45")
            self.horizontalLayout_35.addWidget(self.label_45)
            self.Student_Search_Bar2_6 = QtWidgets.QLineEdit(self.frame_19)
            self.Student_Search_Bar2_6.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Student_Search_Bar2_6.setPlaceholderText("")
            self.Student_Search_Bar2_6.setObjectName("Student_Search_Bar2_6")
            self.horizontalLayout_35.addWidget(self.Student_Search_Bar2_6)
            self.verticalLayout_8.addWidget(self.frame_19)
            self.pushButton_2 = QtWidgets.QPushButton(self.frame_15)
            self.pushButton_2.setStyleSheet("QPushButton {\n"
    "    border: 2px solid rgb(51,51,51);\n"
    "    border-radius: 5px;    \n"
    "    color:rgb(255,255,255);\n"
    "    background-color: rgb(51,51,51);\n"
    "    background-color: rgb(0,143,150);\n"
    "\n"
    "}\n"
    "QPushButton:hover {\n"
    "    \n"
    "    background-color: rgb(0, 255, 255);\n"
    "}\n"
    "QPushButton:pressed {    \n"
    "    border: 2px solid rgb(0,143,150);\n"
    "    background-color: rgb(51,51,51);\n"
    "}\n"
    "\n"
    "QPushButton:disabled {    \n"
    "    border-radius: 5px;    \n"
    "    border: 2px solid rgb(112,112,112);\n"
    "    background-color: rgb(112,112,112);\n"
    "}")
            self.pushButton_2.setObjectName("pushButton_2")
            self.verticalLayout_8.addWidget(self.pushButton_2)
            self.horizontalLayout_8.addWidget(self.frame_15)
            self.Class_Search_Bar3_Btn.addTab(self.tab, icon1, "")
            self.horizontalLayout_3.addWidget(self.Class_Search_Bar3_Btn)
            self.mainBodyTabs.addWidget(self.page_2)
            self.StudentPage = QtWidgets.QWidget()
            self.StudentPage.setObjectName("StudentPage")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.StudentPage)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.frame_23 = QtWidgets.QFrame(self.StudentPage)
            self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_23.setObjectName("frame_23")
            self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_23)
            self.verticalLayout_16.setObjectName("verticalLayout_16")
            self.Student_Tab = QtWidgets.QTabWidget(self.frame_23)
            self.Student_Tab.setStyleSheet("")
            self.Student_Tab.setIconSize(QtCore.QSize(12, 12))
            self.Student_Tab.setObjectName("Student_Tab")
            self.Search_Student_Tab = QtWidgets.QWidget()
            self.Search_Student_Tab.setObjectName("Search_Student_Tab")
            self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Search_Student_Tab)
            self.verticalLayout_4.setObjectName("verticalLayout_4")
            self.frame_8 = QtWidgets.QFrame(self.Search_Student_Tab)
            self.frame_8.setMaximumSize(QtCore.QSize(16777215, 80))
            self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_8.setObjectName("frame_8")
            self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
            self.horizontalLayout_6.setObjectName("horizontalLayout_6")
            self.Student_SearchBar = QtWidgets.QLineEdit(self.frame_8)
            self.Student_SearchBar.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Student_SearchBar.setObjectName("Student_SearchBar")
            self.horizontalLayout_6.addWidget(self.Student_SearchBar)
            self.Student_Search_Btn = QtWidgets.QPushButton(self.frame_8)
            self.Student_Search_Btn.setStyleSheet("QPushButton {\n"
    "    border: 2px solid rgb(51,51,51);\n"
    "    border-radius: 5px;    \n"
    "    color:rgb(255,255,255);\n"
    "    background-color: rgb(51,51,51);\n"
    "    background-color: rgb(0,143,150);\n"
    "padding:9px\n"
    "\n"
    "}\n"
    "QPushButton:hover {\n"
    "    \n"
    "    background-color: rgb(0, 255, 255);\n"
    "}\n"
    "QPushButton:pressed {    \n"
    "    border: 2px solid rgb(0,143,150);\n"
    "    background-color: rgb(51,51,51);\n"
    "}\n"
    "\n"
    "QPushButton:disabled {    \n"
    "    border-radius: 5px;    \n"
    "    border: 2px solid rgb(112,112,112);\n"
    "    background-color: rgb(112,112,112);\n"
    "}")
            self.Student_Search_Btn.setText("")
            self.Student_Search_Btn.setIcon(icon2)
            self.Student_Search_Btn.setObjectName("Student_Search_Btn")
            self.horizontalLayout_6.addWidget(self.Student_Search_Btn)
            self.verticalLayout_4.addWidget(self.frame_8)
            self.frame_14 = QtWidgets.QFrame(self.Search_Student_Tab)
            self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_14.setObjectName("frame_14")
            self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_14)
            self.horizontalLayout_30.setObjectName("horizontalLayout_30")
            self.gridLayout_9 = QtWidgets.QGridLayout()
            self.gridLayout_9.setObjectName("gridLayout_9")
            self.frame_47 = QtWidgets.QFrame(self.frame_14)
            self.frame_47.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_47.setObjectName("frame_47")
            self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_47)
            self.horizontalLayout_13.setObjectName("horizontalLayout_13")
            self.label_35 = QtWidgets.QLabel(self.frame_47)
            self.label_35.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_35.setObjectName("label_35")
            self.horizontalLayout_13.addWidget(self.label_35)
            self.label_11 = QtWidgets.QLabel(self.frame_47)
            self.label_11.setMinimumSize(QtCore.QSize(200, 0))
            self.label_11.setMaximumSize(QtCore.QSize(300, 40))
            self.label_11.setStyleSheet("QLabel {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QLabel:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QLabel:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.label_11.setObjectName("label_11")
            self.horizontalLayout_13.addWidget(self.label_11)
            self.gridLayout_9.addWidget(self.frame_47, 0, 2, 1, 1)
            self.frame_48 = QtWidgets.QFrame(self.frame_14)
            self.frame_48.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_48.setObjectName("frame_48")
            self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_48)
            self.horizontalLayout_19.setObjectName("horizontalLayout_19")
            self.label_36 = QtWidgets.QLabel(self.frame_48)
            self.label_36.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_36.setObjectName("label_36")
            self.horizontalLayout_19.addWidget(self.label_36)
            self.label_16 = QtWidgets.QLabel(self.frame_48)
            self.label_16.setMinimumSize(QtCore.QSize(200, 0))
            self.label_16.setMaximumSize(QtCore.QSize(300, 40))
            self.label_16.setStyleSheet("QLabel {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QLabel:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QLabel:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "")
            self.label_16.setObjectName("label_16")
            self.horizontalLayout_19.addWidget(self.label_16)
            self.gridLayout_9.addWidget(self.frame_48, 3, 3, 1, 1)
            self.frame_49 = QtWidgets.QFrame(self.frame_14)
            self.frame_49.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_49.setObjectName("frame_49")
            self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_49)
            self.horizontalLayout_11.setObjectName("horizontalLayout_11")
            self.label_37 = QtWidgets.QLabel(self.frame_49)
            self.label_37.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_37.setObjectName("label_37")
            self.horizontalLayout_11.addWidget(self.label_37)
            self.label_14 = QtWidgets.QLabel(self.frame_49)
            self.label_14.setMinimumSize(QtCore.QSize(480, 0))
            self.label_14.setMaximumSize(QtCore.QSize(300, 40))
            self.label_14.setStyleSheet("QLabel {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QLabel:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QLabel:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "")
            self.label_14.setObjectName("label_14")
            self.horizontalLayout_11.addWidget(self.label_14)
            self.gridLayout_9.addWidget(self.frame_49, 2, 2, 1, 2)
            self.frame_50 = QtWidgets.QFrame(self.frame_14)
            self.frame_50.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_50.setObjectName("frame_50")
            self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_50)
            self.horizontalLayout_14.setObjectName("horizontalLayout_14")
            self.label_38 = QtWidgets.QLabel(self.frame_50)
            self.label_38.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_38.setObjectName("label_38")
            self.horizontalLayout_14.addWidget(self.label_38)
            self.label_15 = QtWidgets.QLabel(self.frame_50)
            self.label_15.setMinimumSize(QtCore.QSize(200, 0))
            self.label_15.setMaximumSize(QtCore.QSize(300, 40))
            self.label_15.setStyleSheet("QLabel {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QLabel:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QLabel:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "")
            self.label_15.setObjectName("label_15")
            self.horizontalLayout_14.addWidget(self.label_15)
            self.gridLayout_9.addWidget(self.frame_50, 3, 2, 1, 1)
            self.frame_52 = QtWidgets.QFrame(self.frame_14)
            self.frame_52.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_52.setObjectName("frame_52")
            self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_52)
            self.horizontalLayout_9.setObjectName("horizontalLayout_9")
            self.label_12 = QtWidgets.QLabel(self.frame_52)
            self.label_12.setMinimumSize(QtCore.QSize(200, 0))
            self.label_12.setMaximumSize(QtCore.QSize(300, 40))
            self.label_12.setStyleSheet("QLabel {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QLabel:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QLabel:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "")
            self.label_12.setObjectName("label_12")
            self.horizontalLayout_9.addWidget(self.label_12)
            self.gridLayout_9.addWidget(self.frame_52, 0, 3, 1, 1)
            self.frame_53 = QtWidgets.QFrame(self.frame_14)
            self.frame_53.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_53.setObjectName("frame_53")
            self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_53)
            self.horizontalLayout_10.setObjectName("horizontalLayout_10")
            self.label_39 = QtWidgets.QLabel(self.frame_53)
            self.label_39.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_39.setObjectName("label_39")
            self.horizontalLayout_10.addWidget(self.label_39)
            self.label_13 = QtWidgets.QLabel(self.frame_53)
            self.label_13.setMinimumSize(QtCore.QSize(480, 0))
            self.label_13.setMaximumSize(QtCore.QSize(300, 40))
            self.label_13.setStyleSheet("QLabel {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QLabel:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QLabel:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "")
            self.label_13.setObjectName("label_13")
            self.horizontalLayout_10.addWidget(self.label_13)
            self.gridLayout_9.addWidget(self.frame_53, 1, 2, 1, 2)
            self.horizontalLayout_30.addLayout(self.gridLayout_9)
            self.verticalLayout_4.addWidget(self.frame_14)
            self.Student_Tab.addTab(self.Search_Student_Tab, icon2, "")
            self.Add_Student_Tab = QtWidgets.QWidget()
            self.Add_Student_Tab.setObjectName("Add_Student_Tab")
            self.verticalLayout = QtWidgets.QVBoxLayout(self.Add_Student_Tab)
            self.verticalLayout.setObjectName("verticalLayout")
            self.gridLayout_8 = QtWidgets.QGridLayout()
            self.gridLayout_8.setObjectName("gridLayout_8")
            self.frame_46 = QtWidgets.QFrame(self.Add_Student_Tab)
            self.frame_46.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_46.setObjectName("frame_46")
            self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_46)
            self.horizontalLayout_12.setObjectName("horizontalLayout_12")
            self.label_34 = QtWidgets.QLabel(self.frame_46)
            self.label_34.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_34.setObjectName("label_34")
            self.horizontalLayout_12.addWidget(self.label_34)
            self.Student_FName_LineEdit = QtWidgets.QLineEdit(self.frame_46)
            self.Student_FName_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
            self.Student_FName_LineEdit.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Student_FName_LineEdit.setObjectName("Student_FName_LineEdit")
            self.horizontalLayout_12.addWidget(self.Student_FName_LineEdit)
            self.gridLayout_8.addWidget(self.frame_46, 0, 2, 1, 1)
            self.frame_44 = QtWidgets.QFrame(self.Add_Student_Tab)
            self.frame_44.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_44.setObjectName("frame_44")
            self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_44)
            self.horizontalLayout_25.setObjectName("horizontalLayout_25")
            self.label_32 = QtWidgets.QLabel(self.frame_44)
            self.label_32.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_32.setObjectName("label_32")
            self.horizontalLayout_25.addWidget(self.label_32)
            self.Student_Age_SpinBox = QtWidgets.QSpinBox(self.frame_44)
            self.Student_Age_SpinBox.setMinimumSize(QtCore.QSize(100, 26))
            self.Student_Age_SpinBox.setStyleSheet("QSpinBox {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30); \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "\n"
    "QSpinBox:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "}\n"
    "\n"
    "QSpinBox:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "\n"
    "QSpinBox::up-button {\n"
    "    subcontrol-origin: border;\n"
    "    subcontrol-position: top right;\n"
    "    border: 2px solid rgb(74, 148, 146); \n"
    "    width: 16px; /* Adjust button width */\n"
    "    \n"
    "}\n"
    "\n"
    "QSpinBox::down-button {\n"
    "    subcontrol-origin: border;\n"
    "    subcontrol-position: bottom right;\n"
    "    width: 16px; /* Adjust button width */\n"
    "    border: 2px solid rgb(74, 148, 146); \n"
    "    \n"
    "}\n"
    "\n"
    "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
    "    background-color: rgba(255, 255, 255, 0.1); \n"
    "border: 2px solid rgb(0, 255, 255);\n"
    "\n"
    "}\n"
    "QSpinBox::up-button:focus, QSpinBox::down-button:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}\n"
    "")
            self.Student_Age_SpinBox.setObjectName("Student_Age_SpinBox")
            self.horizontalLayout_25.addWidget(self.Student_Age_SpinBox, 0, QtCore.Qt.AlignHCenter)
            self.gridLayout_8.addWidget(self.frame_44, 3, 3, 1, 1)
            self.frame_45 = QtWidgets.QFrame(self.Add_Student_Tab)
            self.frame_45.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_45.setObjectName("frame_45")
            self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_45)
            self.horizontalLayout_26.setObjectName("horizontalLayout_26")
            self.label_33 = QtWidgets.QLabel(self.frame_45)
            self.label_33.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_33.setObjectName("label_33")
            self.horizontalLayout_26.addWidget(self.label_33)
            self.Student_Email_LineEdit = QtWidgets.QLineEdit(self.frame_45)
            self.Student_Email_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
            self.Student_Email_LineEdit.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Student_Email_LineEdit.setObjectName("Student_Email_LineEdit")
            self.horizontalLayout_26.addWidget(self.Student_Email_LineEdit)
            self.gridLayout_8.addWidget(self.frame_45, 2, 2, 1, 2)
            self.frame_43 = QtWidgets.QFrame(self.Add_Student_Tab)
            self.frame_43.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_43.setObjectName("frame_43")
            self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_43)
            self.horizontalLayout_24.setObjectName("horizontalLayout_24")
            self.label_31 = QtWidgets.QLabel(self.frame_43)
            self.label_31.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_31.setObjectName("label_31")
            self.horizontalLayout_24.addWidget(self.label_31)
            self.Student_Grade_LineEdit = QtWidgets.QLineEdit(self.frame_43)
            self.Student_Grade_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
            self.Student_Grade_LineEdit.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Student_Grade_LineEdit.setObjectName("Student_Grade_LineEdit")
            self.horizontalLayout_24.addWidget(self.Student_Grade_LineEdit)
            self.gridLayout_8.addWidget(self.frame_43, 3, 2, 1, 1)
            self.frame_41 = QtWidgets.QFrame(self.Add_Student_Tab)
            self.frame_41.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_41.setObjectName("frame_41")
            self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_41)
            self.verticalLayout_21.setObjectName("verticalLayout_21")
            self.Student_LName_LineEdit = QtWidgets.QLineEdit(self.frame_41)
            self.Student_LName_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
            self.Student_LName_LineEdit.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Student_LName_LineEdit.setObjectName("Student_LName_LineEdit")
            self.verticalLayout_21.addWidget(self.Student_LName_LineEdit)
            self.gridLayout_8.addWidget(self.frame_41, 0, 3, 1, 1)
            self.frame_42 = QtWidgets.QFrame(self.Add_Student_Tab)
            self.frame_42.setStyleSheet(" border: 2px solid transparent; /* Set border color to transparent */")
            self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_42.setObjectName("frame_42")
            self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_42)
            self.horizontalLayout_23.setObjectName("horizontalLayout_23")
            self.label_30 = QtWidgets.QLabel(self.frame_42)
            self.label_30.setStyleSheet("font: 81 italic 13pt \"Lato Heavy\";")
            self.label_30.setObjectName("label_30")
            self.horizontalLayout_23.addWidget(self.label_30)
            self.Student_Mobile_LineEdit = QtWidgets.QLineEdit(self.frame_42)
            self.Student_Mobile_LineEdit.setMinimumSize(QtCore.QSize(0, 26))
            self.Student_Mobile_LineEdit.setStyleSheet("QLineEdit {\n"
    "    border: 2px solid rgb(74, 148, 146);\n"
    "    border-radius: 5px;\n"
    "    padding: 10px;\n"
    "    background-color: rgb(30, 30, 30);    \n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "QLineEdit:hover {\n"
    "    border: 2px solid rgb(0, 255, 255);\n"
    "   \n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border: 2px solid rgb(255, 255, 0);\n"
    "    color: rgb(250, 250, 250);\n"
    "}")
            self.Student_Mobile_LineEdit.setObjectName("Student_Mobile_LineEdit")
            self.horizontalLayout_23.addWidget(self.Student_Mobile_LineEdit)
            self.gridLayout_8.addWidget(self.frame_42, 1, 2, 1, 2)
            self.verticalLayout.addLayout(self.gridLayout_8)
            self.Student_Add_Btn = QtWidgets.QPushButton(self.Add_Student_Tab)
            self.Student_Add_Btn.setStyleSheet("QPushButton {\n"
    "    border: 2px solid rgb(51,51,51);\n"
    "    border-radius: 5px;    \n"
    "    color:rgb(255,255,255);\n"
    "    background-color: rgb(51,51,51);\n"
    "    background-color: rgb(0,143,150);\n"
    "\n"
    "}\n"
    "QPushButton:hover {\n"
    "    \n"
    "    background-color: rgb(0, 255, 255);\n"
    "}\n"
    "QPushButton:pressed {    \n"
    "    border: 2px solid rgb(0,143,150);\n"
    "    background-color: rgb(51,51,51);\n"
    "}\n"
    "\n"
    "QPushButton:disabled {    \n"
    "    border-radius: 5px;    \n"
    "    border: 2px solid rgb(112,112,112);\n"
    "    background-color: rgb(112,112,112);\n"
    "}")
            self.Student_Add_Btn.setObjectName("Student_Add_Btn")
            self.verticalLayout.addWidget(self.Student_Add_Btn)
            self.Student_Tab.addTab(self.Add_Student_Tab, icon1, "")
            self.verticalLayout_16.addWidget(self.Student_Tab)
            self.horizontalLayout_4.addWidget(self.frame_23)
            self.mainBodyTabs.addWidget(self.StudentPage)
            self.gridLayout_10.addWidget(self.mainBodyTabs, 0, 1, 1, 1)
            self.frame_33 = QtWidgets.QFrame(self.frame_6)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(200)
            sizePolicy.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
            self.frame_33.setSizePolicy(sizePolicy)
            self.frame_33.setMinimumSize(QtCore.QSize(200, 300))
            self.frame_33.setMaximumSize(QtCore.QSize(200, 16777215))
            self.frame_33.setStyleSheet("background-color: rgb(56, 56, 56);")
            self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_33.setObjectName("frame_33")
            self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_33)
            self.verticalLayout_6.setObjectName("verticalLayout_6")
            self.frame_51 = QtWidgets.QFrame(self.frame_33)
            self.frame_51.setMinimumSize(QtCore.QSize(170, 40))
            self.frame_51.setMaximumSize(QtCore.QSize(170, 40))
            self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_51.setObjectName("frame_51")
            self.Dashboard_Btn = QtWidgets.QPushButton(self.frame_51)
            self.Dashboard_Btn.setGeometry(QtCore.QRect(0, 0, 170, 40))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Dashboard_Btn.sizePolicy().hasHeightForWidth())
            self.Dashboard_Btn.setSizePolicy(sizePolicy)
            self.Dashboard_Btn.setMinimumSize(QtCore.QSize(170, 40))
            self.Dashboard_Btn.setMaximumSize(QtCore.QSize(200, 0))
            font = QtGui.QFont()
            font.setFamily("Poppins")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Dashboard_Btn.setFont(font)
            self.Dashboard_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.Dashboard_Btn.setStyleSheet("/* STYLESHEET FOR PUSH BUTTON: START, SAVE, CLOSE, RESTORE, CONNECT, EDIT */\n"
    " QPushButton {\n"
    " border: 2px solid rgb(51,51,51);\n"
    " border-radius: 5px; \n"
    "color:rgb(255,255,255);\n"
    " background-color: rgb(51,51,51);\n"
    " }\n"
    " QPushButton:hover {\n"
    " border: 2px solid rgb(0,143,150);\n"
    " background-color: rgb(0,143,150);\n"
    " }\n"
    " QPushButton:pressed {   \n"
    "border: 2px solid rgb(0,143,150);\n"
    " background-color: rgb(51,51,51);\n"
    " }\n"
    " QPushButton:disabled {  \n"
    "border-radius: 5px; \n"
    "border: 2px solid rgb(112,112,112);\n"
    " background-color: rgb(112,112,112);\n"
    " }\n"
    " /* SEE THE EFFECT BELOW*/")
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap(":/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Dashboard_Btn.setIcon(icon4)
            self.Dashboard_Btn.setIconSize(QtCore.QSize(28, 28))
            self.Dashboard_Btn.setCheckable(True)
            self.Dashboard_Btn.setObjectName("Dashboard_Btn")
            self.verticalLayout_6.addWidget(self.frame_51)
            self.studentsFrame_6 = QtWidgets.QFrame(self.frame_33)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.studentsFrame_6.sizePolicy().hasHeightForWidth())
            self.studentsFrame_6.setSizePolicy(sizePolicy)
            self.studentsFrame_6.setMinimumSize(QtCore.QSize(170, 40))
            self.studentsFrame_6.setMaximumSize(QtCore.QSize(200, 40))
            self.studentsFrame_6.setStyleSheet("border: none;\n"
    "\n"
    "border-top-right-radius:7px;\n"
    "border-bottom-right-radius:7px;")
            self.studentsFrame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.studentsFrame_6.setFrameShadow(QtWidgets.QFrame.Raised)
            self.studentsFrame_6.setObjectName("studentsFrame_6")
            self.Students_Btn = QtWidgets.QPushButton(self.studentsFrame_6)
            self.Students_Btn.setGeometry(QtCore.QRect(0, 0, 171, 40))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Students_Btn.sizePolicy().hasHeightForWidth())
            self.Students_Btn.setSizePolicy(sizePolicy)
            self.Students_Btn.setMinimumSize(QtCore.QSize(160, 40))
            self.Students_Btn.setMaximumSize(QtCore.QSize(200, 0))
            font = QtGui.QFont()
            font.setFamily("Poppins")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Students_Btn.setFont(font)
            self.Students_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.Students_Btn.setStyleSheet("/* STYLESHEET FOR PUSH BUTTON: START, SAVE, CLOSE, RESTORE, CONNECT, EDIT */\n"
    " QPushButton {\n"
    " border: 2px solid rgb(51,51,51);\n"
    " border-radius: 5px; \n"
    "color:rgb(255,255,255);\n"
    " background-color: rgb(51,51,51);\n"
    " }\n"
    " QPushButton:hover {\n"
    " border: 2px solid rgb(0,143,150);\n"
    " background-color: rgb(0,143,150);\n"
    " }\n"
    " QPushButton:pressed {   \n"
    "border: 2px solid rgb(0,143,150);\n"
    " background-color: rgb(51,51,51);\n"
    " }\n"
    " QPushButton:disabled {  \n"
    "border-radius: 5px; \n"
    "border: 2px solid rgb(112,112,112);\n"
    " background-color: rgb(112,112,112);\n"
    " }\n"
    " /* SEE THE EFFECT BELOW*/")
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap(":/icons/Student.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Students_Btn.setIcon(icon5)
            self.Students_Btn.setIconSize(QtCore.QSize(28, 28))
            self.Students_Btn.setCheckable(True)
            self.Students_Btn.setObjectName("Students_Btn")
            self.verticalLayout_6.addWidget(self.studentsFrame_6)
            self.staffFrame_6 = QtWidgets.QFrame(self.frame_33)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.staffFrame_6.sizePolicy().hasHeightForWidth())
            self.staffFrame_6.setSizePolicy(sizePolicy)
            self.staffFrame_6.setMinimumSize(QtCore.QSize(170, 40))
            self.staffFrame_6.setMaximumSize(QtCore.QSize(200, 40))
            self.staffFrame_6.setStyleSheet("border: none;\n"
    "\n"
    "border-top-right-radius:7px;\n"
    "border-bottom-right-radius:7px;")
            self.staffFrame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.staffFrame_6.setFrameShadow(QtWidgets.QFrame.Raised)
            self.staffFrame_6.setObjectName("staffFrame_6")
            self.Staff_Btn = QtWidgets.QPushButton(self.staffFrame_6)
            self.Staff_Btn.setGeometry(QtCore.QRect(0, 0, 171, 40))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Staff_Btn.sizePolicy().hasHeightForWidth())
            self.Staff_Btn.setSizePolicy(sizePolicy)
            self.Staff_Btn.setMinimumSize(QtCore.QSize(0, 40))
            self.Staff_Btn.setMaximumSize(QtCore.QSize(200, 0))
            font = QtGui.QFont()
            font.setFamily("Poppins")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Staff_Btn.setFont(font)
            self.Staff_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.Staff_Btn.setStyleSheet("/* STYLESHEET FOR PUSH BUTTON: START, SAVE, CLOSE, RESTORE, CONNECT, EDIT */\n"
    " QPushButton {\n"
    " border: 2px solid rgb(51,51,51);\n"
    " border-radius: 5px; \n"
    "color:rgb(255,255,255);\n"
    " background-color: rgb(51,51,51);\n"
    " }\n"
    " QPushButton:hover {\n"
    " border: 2px solid rgb(0,143,150);\n"
    " background-color: rgb(0,143,150);\n"
    " }\n"
    " QPushButton:pressed {   \n"
    "border: 2px solid rgb(0,143,150);\n"
    " background-color: rgb(51,51,51);\n"
    " }\n"
    " QPushButton:disabled {  \n"
    "border-radius: 5px; \n"
    "border: 2px solid rgb(112,112,112);\n"
    " background-color: rgb(112,112,112);\n"
    " }\n"
    " /* SEE THE EFFECT BELOW*/")
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap(":/icons/staff.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Staff_Btn.setIcon(icon6)
            self.Staff_Btn.setIconSize(QtCore.QSize(32, 32))
            self.Staff_Btn.setCheckable(True)
            self.Staff_Btn.setObjectName("Staff_Btn")
            self.verticalLayout_6.addWidget(self.staffFrame_6)
            self.frame_11 = QtWidgets.QFrame(self.frame_33)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
            self.frame_11.setSizePolicy(sizePolicy)
            self.frame_11.setMinimumSize(QtCore.QSize(170, 40))
            self.frame_11.setMaximumSize(QtCore.QSize(200, 40))
            self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_11.setObjectName("frame_11")
            self.Class_Btn = QtWidgets.QPushButton(self.frame_11)
            self.Class_Btn.setGeometry(QtCore.QRect(0, 0, 181, 40))
            self.Class_Btn.setMinimumSize(QtCore.QSize(0, 40))
            self.Class_Btn.setMaximumSize(QtCore.QSize(200, 0))
            font = QtGui.QFont()
            font.setFamily("Lato Heavy")
            font.setPointSize(10)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            self.Class_Btn.setFont(font)
            self.Class_Btn.setStyleSheet("/* STYLESHEET FOR PUSH BUTTON: START, SAVE, CLOSE, RESTORE, CONNECT, EDIT */\n"
    " QPushButton {\n"
    " border: 2px solid rgb(51,51,51);\n"
    " border-radius: 5px; \n"
    "color:rgb(255,255,255);\n"
    " background-color: rgb(51,51,51);\n"
    " }\n"
    " QPushButton:hover {\n"
    " border: 2px solid rgb(0,143,150);\n"
    " background-color: rgb(0,143,150);\n"
    " }\n"
    " QPushButton:pressed {   \n"
    "border: 2px solid rgb(0,143,150);\n"
    " background-color: rgb(51,51,51);\n"
    " }\n"
    " QPushButton:disabled {  \n"
    "border-radius: 5px; \n"
    "border: 2px solid rgb(112,112,112);\n"
    " background-color: rgb(112,112,112);\n"
    " }\n"
    " /* SEE THE EFFECT BELOW*/")
            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap(":/icons/Class.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Class_Btn.setIcon(icon7)
            self.Class_Btn.setIconSize(QtCore.QSize(28, 28))
            self.Class_Btn.setObjectName("Class_Btn")
            self.verticalLayout_6.addWidget(self.frame_11)
            self.gridLayout_10.addWidget(self.frame_33, 0, 0, 1, 1)
            self.gridLayout_11.addWidget(self.frame_6, 1, 0, 1, 1)
            self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 20))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)
            ############
            self.Students_Btn.clicked.connect(self.goToPage2)

            self.Student_Add_Btn.clicked.connect(self.add_student)
            self.Student_Search_Btn.clicked.connect(self.student_search)
            self.Prof_Add_Btn.clicked.connect(self.add_prof)
            self.Student_Search_Btn_2.clicked.connect(self.prof_search)
            self.Staff_Btn.clicked.connect(self.goToPage_prof)
            self.Class_Btn.clicked.connect(self.goToPage_class)
            self.Add_Student_Class_Btn.clicked.connect(self.add_stud_class)
            self.Add_Prof_Class_Btn.clicked.connect(self.add_prof_class)
            self.Student_Search_Btn_7.clicked.connect(self.search_class)
            self.pushButton_2.clicked.connect(self.add_class)
            self.Dashboard_Btn.clicked.connect(self.goToPage_dash)
            self.class_search_result.itemClicked.connect(self.handle_item_click)
            self.professor_TW.itemClicked.connect(self.handle_prof_item_click)
            self.create_line_chart_in_graphics_view()



            ###########

            self.retranslateUi(MainWindow)
            self.mainBodyTabs.setCurrentIndex(0)
            self.Prof_Tab.setCurrentIndex(0)
            self.Class_Search_Bar3_Btn.setCurrentIndex(2)
            self.Student_Tab.setCurrentIndex(0)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.label_20.setText(_translate("MainWindow", "mobile"))
            self.label_21.setText(_translate("MainWindow", "title"))
            self.label_22.setText(_translate("MainWindow", "age"))
            self.label_23.setText(_translate("MainWindow", "email"))
            self.profName_lab.setText(_translate("MainWindow", "name"))
            self.Prof_Add_Btn.setText(_translate("MainWindow", "Add"))
            self.Prof_Tab.setTabText(self.Prof_Tab.indexOf(self.Add_Prof_Tab), _translate("MainWindow", "Add Professor"))
            self.label_40.setText(_translate("MainWindow", "name"))
            self.label_17.setText(_translate("MainWindow", "TextLabel"))
            self.label_41.setText(_translate("MainWindow", "age"))
            self.label_18.setText(_translate("MainWindow", "TextLabel"))
            self.label_42.setText(_translate("MainWindow", "email"))
            self.label_19.setText(_translate("MainWindow", "TextLabel"))
            self.label_43.setText(_translate("MainWindow", "Title"))
            self.label_24.setText(_translate("MainWindow", "TextLabel"))
            self.label_25.setText(_translate("MainWindow", "TextLabel"))
            self.label_44.setText(_translate("MainWindow", "mobile"))
            self.label_26.setText(_translate("MainWindow", "TextLabel"))
            self.Prof_Tab.setTabText(self.Prof_Tab.indexOf(self.Search_Prof_Tab), _translate("MainWindow", "search"))
            self.Prof_Search_Bar2.setPlaceholderText(_translate("MainWindow", "search for a Professor"))
            self.Class_Search_Bar2.setPlaceholderText(_translate("MainWindow", "search for a class"))
            self.Add_Prof_Class_Btn.setText(_translate("MainWindow", "add professor to class"))
            self.Class_Search_Bar3_Btn.setTabText(self.Class_Search_Bar3_Btn.indexOf(self.Add_Prof_Class_Tab), _translate("MainWindow", "Add Professor to Class"))
            self.Add_Student_Class_Btn.setText(_translate("MainWindow", "Add Student to Class"))
            self.Class_Search_Bar3.setPlaceholderText(_translate("MainWindow", "search for a Class"))
            self.Student_Search_Bar2.setPlaceholderText(_translate("MainWindow", "search fo a student"))
            self.Class_Search_Bar3_Btn.setTabText(self.Class_Search_Bar3_Btn.indexOf(self.Add_Student_Class_Tab), _translate("MainWindow", "Add Student to Class"))
            self.Class_Search_Bar3_Btn.setTabText(self.Class_Search_Bar3_Btn.indexOf(self.Sarch_Class_Tab), _translate("MainWindow", "search"))
            self.label_27.setText(_translate("MainWindow", "class name"))
            self.label_28.setText(_translate("MainWindow", "class code   "))
            self.label_29.setText(_translate("MainWindow", "lecture hall"))
            self.label_45.setText(_translate("MainWindow", " time           "))
            self.pushButton_2.setText(_translate("MainWindow", "Add class"))
            self.Class_Search_Bar3_Btn.setTabText(self.Class_Search_Bar3_Btn.indexOf(self.tab), _translate("MainWindow", "add class"))
            self.label_35.setText(_translate("MainWindow", "name"))
            self.label_11.setText(_translate("MainWindow", "TextLabel"))
            self.label_36.setText(_translate("MainWindow", "age"))
            self.label_16.setText(_translate("MainWindow", "TextLabel"))
            self.label_37.setText(_translate("MainWindow", "email"))
            self.label_14.setText(_translate("MainWindow", "TextLabel"))
            self.label_38.setText(_translate("MainWindow", "grade"))
            self.label_15.setText(_translate("MainWindow", "TextLabel"))
            self.label_12.setText(_translate("MainWindow", "TextLabel"))
            self.label_39.setText(_translate("MainWindow", "mobile"))
            self.label_13.setText(_translate("MainWindow", "TextLabel"))
            self.Student_Tab.setTabText(self.Student_Tab.indexOf(self.Search_Student_Tab), _translate("MainWindow", "search"))
            self.label_34.setText(_translate("MainWindow", "name"))
            self.label_32.setText(_translate("MainWindow", "age"))
            self.label_33.setText(_translate("MainWindow", "email"))
            self.label_31.setText(_translate("MainWindow", "grade"))
            self.label_30.setText(_translate("MainWindow", "mobile"))
            self.Student_Add_Btn.setText(_translate("MainWindow", "Add"))
            self.Student_Tab.setTabText(self.Student_Tab.indexOf(self.Add_Student_Tab), _translate("MainWindow", "Add Student"))
            self.Dashboard_Btn.setText(_translate("MainWindow", "Home"))
            self.Students_Btn.setText(_translate("MainWindow", "Students"))
            self.Staff_Btn.setText(_translate("MainWindow", "Staff"))
            self.Class_Btn.setText(_translate("MainWindow", "Class"))
