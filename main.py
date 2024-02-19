from PyQt5 import QtCore, QtGui, QtWidgets
from learning_management.student import Student
from learning_management.Person import Person




from board import Ui_MainWindow
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
