class Course:
    def __init__(self, courseID):
        self.courseID = courseID
        self.courseName = ""
        self.totalGrade = 0
        self.lectureHall = ""
        self.lectureDay = 0
        self.lectureTime = 0
        self.department = ""
        self.totalGrades = 0.0
        self.totalStudents = 0
        self.averageGrade = 0.0
        self.passedStudents = 0
        self.passRatio = 0.0
        self.students = {}
        self.staff = []

    def getCourseID(self):
        return self.courseID

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
