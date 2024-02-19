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

# def add_student(Ui_MainWindow):
    
    
    # student_FName =Ui_MainWindow.Student_FName_LineEdit.text()
    # student_LName =Ui_MainWindow.Student_LName_LineEdit.text()
    # student_Mobile =Ui_MainWindow.Student_Mobile_LineEdit.text()
    # student_Email =Ui_MainWindow.Student_Email_LineEdit.text()
    # student_Grade =Ui_MainWindow.Student_Grade_LineEdit.text()
    # student_Age =Ui_MainWindow.Student_Age_SpinBox.text()
    # stud = Student(student_FName, student_LName, student_Mobile ,  student_Age , student_Mobile, student_Email,student_Grade )
    # attribute_values= []
    # for attr_name , attr_value in stud.__dict__.items():
    #     attribute_values.append(attr_value)
    # stud.append_value('student_FName'+' '+'student_LName' , attribute_values)
    
# def search_student(self):
#     search_name = self.Student_SearchBar.text()
#     stud = Student.search(search_name)
#     self.label_11setText(stud.)
    
