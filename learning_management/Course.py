import csv
from learning_management.Person import Person
from learning_management.student import Student
class Course:
    representation_course= {}
    file_name = 'class.csv'
    def __init__(self, course_name , hall , course_code, course_time): #, hall , course_code, course_time
        self.courseName = course_name
        self.hall = hall
        self.course_code = course_code
        self.course_time =course_time
        # students_string=','.join(self.students)
        # students_string=','.join(self.students)
        # # self.data = [course_name , hall , course_code, course_time,f"({self.students}), f"({self.staff})]

    def add_stud_toClass(cls,student_full_name , class_name):
        student_data = Student.search(student_full_name)
        

    

    def search(cls, name):
        # if name in cls.representation_student:
        #     return cls.representation_student[name]
        # else:
        #     # If the key doesn't exist, raise an error or handle it accordingly
        #     raise KeyError(f"student '{name}' not found")
        with open('course.csv', "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['course_name'])
                if row['course_name'] == name:
                    
                    return row
            else:
                raise KeyError(f"course '{name}' not found")

        
    def append_value(cls, key, value, file_name=file_name):
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(value)
        # if there is name duplicated also append as a list
        cls.representation_course[key] = value

    

    # def getCourseID(self):
    #     return self.courseID

    def getCourseName(self):
        return self.courseName

    def getCourseGrade(self):
        return self.totalGrade

    def getLectureDay(self):
        return self.lectureDay

    def getLectureTime(self):
        return self.lectureTime

    def getCourseDepartment(self):
        return self.department

    def setCourseName(self, courseName):
        self.courseName = courseName

    def setCourseGrade(self, grade):
        self.totalGrade = grade

    def setLectureHall(self, lecHall):
        self.lectureHall = lecHall

    def setLectureDay(self, lecDay):
        self.lectureDay = lecDay

    def setLectureTime(self, lecTime):
        self.lectureTime = lecTime

    def setCourseDepartment(self, department):
        self.department = department
