from person import person


class Admin(person):
    def __init__(self, first_name, last_name, age, mobile, email, adminID, username, password, gender):
        super().__init__(first_name, last_name, age, mobile, email)
        self.adminID = adminID
        self.username = username
        self.password = password
        self.gender = gender

    def adminID(self, adminID):
        self.adminID = adminID

    def getAdminID(self):
        return self.adminID
    
    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    def getGender(self):
        return self.gender
    
    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def setGender(self, gender):
        self.gender = gender