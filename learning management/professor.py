from fileinput import filename
from person import Person
import csv

class professor(Person):
    file_name = 'professors.csv'
    representation_professor= {}
    def __init__(self, first_name, last_name, age, mobile, email,gender, professorID, position, departement, professorCourses):
        super().__init__(first_name, last_name, age, mobile, email)
        self.professorID = professorID
        self.departement = departement
        self.professorCourses = []
        self.gender = gender
        self.position = position
        self.fullName = first_name + ' ' + last_name
    
    def search(cls, key):
        if key in cls.representation_professor:
            return cls.representation_professor[key]
        else:
            # If the key doesn't exist, raise an error or handle it accordingly
            raise KeyError(f"professor '{key}' not found")
        
    def append_value(cls, key, value):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(value)
        cls.representation_professor[key] = value  # if there is name duplicated also append as a list
     # also if the name in not found w append the name as a key and value of his data

    def printing_all_professors(self, file_name):
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def __str__(self):
        return f"(first_name= {self.first_name},last_name= {self.last_name},age= {self.age},mobile= {self.mobile},email= {self.email},gender= {self.gender},professorID= {self.professorID},position= {self.position},departement= {self.departement},professorCourses= {self.professorCourses})"

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