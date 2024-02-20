from fileinput import filename
import pandas as pd
from learning_management.Course import Course
import csv

class Stud_course:
    representation_studentCourses = {}
    def __init__(self, course_name, student_name):
        self.course_name = course_name
        # self.studCourse = stud_course
        self.student_name = student_name
    
    
    
    def append_value(cls, key, value, file_name='student_courses.csv'):
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(value)
        # if there is name duplicated also append as a list
        cls.representation_studentCourses[key] = value
        
    def change_to_df(file_name='student_courses.csv'):
        student_courses = pd.read_csv(file_name)

    def __str__(self):
        return f"(course_name= {self.course_name},student_name= {self.student_name})"
