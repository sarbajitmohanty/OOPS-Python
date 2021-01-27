class Students:
    number_of_students = 0

    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

        Students.number_of_students += 1

    def fullName(self):
        print(self.fname.capitalize() + " " + self.lname.capitalize())

    """
    pass a function to another function and that return a function 
    then it is known as decorator
    """
    @classmethod
    def from_string(cls, data_string):
        firstName, lastName, email = data_string.split('-')
        return cls(firstName, lastName, email)

    @staticmethod
    def print_Students():
        print(Students.number_of_students)

# student1 = Students(" sarbajit", "mohanty", "abc.xyz@gmail.com")
# student1.fullName()
#
# student2 = Students("John", "doe", "pqr.def@gmail.com")
# student2.fullName()

stu1_string = 'sarbajit-mohanty-abc.xyz@gmail.com'
stu2_string = 'john-doe-pqr.def@gmail.com'

stu1 = Students.from_string(stu1_string)

Students.print_Students()
stu1.fullName()