from fileinput import filename
import pandas as pd
from learning_management.Course import Course
import csv


class Prof_course:
    representation_profCourses = {}
    def __init__(self, course_name, professor_name):
        self.course_name = course_name
        # self.studCourse = stud_course
        self.professor_name = professor_name
    
    # def add_stud_course(self,course):
    #     self.studCourse = course
    
    def append_value(cls, key, value, file_name='professor_courses.csv'):
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(value)
        # if there is name duplicated also append as a list
        cls.representation_profCourses[key] = value
    def __str__(self):
        return f"(course_name= {self.course_name},professor_name= {self.professor_name})"


    
    # def get_studCourse(self):
    #     return self.studCourse
    
    # def search_course(cls, course_name):
    #     # if name in cls.representation_student:
    #     #     return cls.representation_student[name]
    #     # else:
    #     #     # If the key doesn't exist, raise an error or handle it accordingly
    #     #     raise KeyError(f"student '{name}' not found")
    #     with open('student_courses.csv', "r") as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             print(row['course_name'])
    #             if row['course_name'] == course_name:
                    
    #                 return row
    #         else:
    #             raise KeyError(f"student '{course_name}' not found")
    
    def change_to_df(file_name='professor_courses.csv'):
        student_courses = pd.read_csv(file_name)
     # def get_studCourse(self):
    #     return self.studCourse
    
    # def search_course(cls, course_name):
    #     # if name in cls.representation_student:
    #     #     return cls.representation_student[name]
    #     # else:
    #     #     # If the key doesn't exist, raise an error or handle it accordingly
    #     #     raise KeyError(f"student '{name}' not found")
    #     with open('student_courses.csv', "r") as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             print(row['course_name'])
    #             if row['course_name'] == course_name:
                    
    #                 return row
    #         else:
    #             raise KeyError(f"student '{course_name}' not found")
    
    def change_to_df(file_name='professor_courses.csv'):
        student_courses = pd.read_csv(file_name)
