from learning_management.Person import Person
import csv


class Student(Person):
    file_name = 'students.csv'
    representation_student = {}

    def __init__(self, first_name, last_name, age, mobile, email, grade):
        super().__init__(first_name, last_name, age, mobile, email)
        self.studentCourses = []
        self.grade = grade
        self.fullName = first_name + ' ' + last_name

    def search(cls, key):
        if key in cls.representation_student:
            return cls.representation_student[key]
        else:
            # If the key doesn't exist, raise an error or handle it accordingly
            raise KeyError(f"student '{key}' not found")

    def append_value(cls, key, value, file_name=file_name):
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(value)
        # if there is name duplicated also append as a list
        cls.representation_student[key] = value
     # also if the name in not found w append the name as a key and value of his data

    def printing_all_students(cls, file_name=file_name):
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def __str__(self):
        return f"(first_name= {self.firstName},last_name= {self.lastName},age= {self.age},mobile= {self.mobile},email= {self.email},grade= {self.grade})"

    # def __repr__(self):
    #     return f"(name='{self.name}', age={self.age})"

    def studentID(self, studentID):
        self.studentID = studentID

    def getStudentID(self):
        return self.studentID

    def getGrade(self):
        return self.grade

    def getDepartement(self):
        return self.departement

    def getGender(self):
        return self.gender

    def getCourses(self):
        return self.staffCourses

    def setGrade(self, grade):
        self.garde = grade

    def setDepartement(self, departement):
        self.departement = departement

    def setGender(self, gender):
        self.gender = gender

    def addCourse(self, course):
        # self.studentCourses = course
        self.studentCourses.append(course)

    def removeCourse(self, course):
        # self.studentCourses = '-'
        self.studentCourses.pop(course)
