# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(340, 340)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.circularProgressBarBase = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBarBase.setGeometry(QtCore.QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")
        self.circularProgress = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularProgress.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(147, 255, 252, 255));\n"
"}")
        self.circularProgress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgress.setObjectName("circularProgress")
        self.circularBg = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.container = QtWidgets.QFrame(self.circularProgressBarBase)
        self.container.setGeometry(QtCore.QRect(25, 25, 270, 270))
        self.container.setStyleSheet("QFrame{\n"
"    border-radius: 135px;\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.layoutWidget = QtWidgets.QWidget(self.container)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 30, 251, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTitle = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("background-color: none;\n"
"color: #FFFFFF")
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)
        self.labelCredits = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labelCredits.setFont(font)
        self.labelCredits.setStyleSheet("background-color: none;\n"
"color: rgb(155, 155, 255);")
        self.labelCredits.setText("")
        self.labelCredits.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits.setObjectName("labelCredits")
        self.gridLayout.addWidget(self.labelCredits, 3, 0, 1, 1)
        self.labelPercentage = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(68)
        self.labelPercentage.setFont(font)
        self.labelPercentage.setStyleSheet("background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentage.setObjectName("labelPercentage")
        self.gridLayout.addWidget(self.labelPercentage, 2, 0, 1, 1)
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.labelTitle.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#74ffef;\">SMS</span></p></body></html>"))
        self.labelPercentage.setText(_translate("SplashScreen", "<html><head/><body><p>0<span style=\" font-size:58pt; color:#8afff6; vertical-align:super;\">%</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplashScreen = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec_())
