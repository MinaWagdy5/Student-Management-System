from PyQt5 import QtCore, QtGui, QtWidgets
from learning_management.student import Student
from learning_management.Person import Person


from board5 import Ui_MainWindow as part1
from FinalBoard import Ui_MainWindow as part2

class Ui_MainWindow(part1, part2):
    pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
