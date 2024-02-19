from fileinput import filename
from learning_management.Person import Person
import csv

class professor(Person):
    file_name = 'professors.csv'
    representation_professor= {}
    def __init__(self, first_name, last_name, age, mobile, email, title):
        super().__init__(first_name, last_name, age, mobile, email)
        self.professorCourses = []
        self.title = title
        self.fullName = first_name + ' ' + last_name
    
    def search(cls, name):
        # if name in cls.representation_student:
        #     return cls.representation_student[name]
        # else:
        #     # If the key doesn't exist, raise an error or handle it accordingly
        #     raise KeyError(f"student '{name}' not found")
        with open('professors.csv', "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['full_name'])
                if row['full_name'] == name:
                    
                    return row
            else:
                raise KeyError(f"professor '{name}' not found")
        
    def append_value(cls, key, value, file_name=file_name):
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(value)
        cls.representation_professor[key] = value  # if there is name duplicated also append as a list
     # also if the name in not found w append the name as a key and value of his data

    def printing_all_professors(cls, file_name= file_name):
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def __str__(self):
        return f"(first_name= {self.firstName},last_name= {self.lastName},age= {self.age},mobile= {self.mobile},email= {self.email},title= {self.title})"
    def professorID(self, professorID):
        self.professorID= professorID

    def getProfessorID(self):
        return self.professorID
    
    def getPosition(self):
        return self.position
    
    def getDepartement(self):
        return self.departement
    
    def getGender(self):
        return self.gender
    
    def getProfessorCourses(self):
        return self.professorCourses
    
    def setPosition(self, position):
        self.position = position

    def setDepartement(self, departement):
        self.departement= departement

    def setGender(self, gender):
        self.gender = gender

    def addCourse(self, course):
        self.professorCourses.append(course)

    def removeCourse(self, course):
        self.professorCourses.pop(course)
