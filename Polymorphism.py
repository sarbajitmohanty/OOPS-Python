class Students:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def fullName(self):
        print(self.fname.capitalize() + " " + self.lname.capitalize())

class Teachers:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def fullName(self):
        print(self.fname.capitalize() + " " + self.lname.capitalize())


student1 = Students("sarbajit", "mohanty", "abc.xyz@gmail.com")
student1.fullName()

student2 = Students("John", "doe", "pqr.def@gmail.com")
student2.fullName()

teacher1 = Teachers("emma", "stone", "emmastone@gmail.com")
teacher1.fullName()