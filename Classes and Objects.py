class Students:

    number_of_students = 0  #this is a class variable
    """whenever a variable inside a class it is known as class variable"""

    def __init__(self, fname, lname, email):  #constructor
        self.fname = fname  #self.fname is an instance variable
        self.lname = lname  #self.lname is an instance variable
        self.email = email  #self.email is an instance variable

        """whenever a variable is refrencing an instance it is known as instance variable"""

        Students.number_of_students += 1  #it will keep the track of number of objects or instances created

    def fullName(self):
        print(self.fname.capitalize() + " " + self.lname.capitalize())


student1 = Students("sarbajit", "mohanty", "abc.xyz@gmail.com")

print(Students.number_of_students) #output will be 1 because the second object is not created yet
student1.fullName()
Students.fullName(student1)



student2 = Students("John", "doe", "pqr.def@gmail.com")

print(Students.number_of_students) #here the output will be 2
student2.fullName()
Students.fullName(student2)
