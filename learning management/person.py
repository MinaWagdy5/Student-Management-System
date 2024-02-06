class Person:
    def __init__(self, first_name, last_name, age, mobile, email):
        self.firstName = first_name
        self.lastName = last_name
        self.age = age
        self.mobile = mobile
        self.email = email

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getAge(self):
        return self.age

    def getMobile(self):
        return self.mobile

    def getEmail(self):
        return self.email

    def setFirstName(self, first_name):
        self.firstName = first_name

    def setLastName(self, last_name):
        self.lastName = last_name

    def setAge(self, age):
        self.age = age

    def setMobile(self, mobile):
        self.mobile = mobile

    def setEmail(self, email):
        self.email = email
