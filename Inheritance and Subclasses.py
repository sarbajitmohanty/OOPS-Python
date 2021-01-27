class UniversityPeople:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def fullName(self):
        print(self.fname.capitalize() + " " + self.lname.capitalize())


class Students(UniversityPeople):
    pass


class Teachers(UniversityPeople):
    def __init__(self, fname, lname, email, salary):
        super().__init__(fname, lname, email)
        self.salary = salary

class Maths(Teachers):
    pass


student1 = Students("sarbajit", "mohanty", "abc.xyz@gmail.com")
student2 = Students("john", "doe", "pqr.def@gmail.com")

teacher1 = Teachers("emma", "stone", "emmastone@gmail.com", "97000")

student1.fullName()
print(teacher1.salary)

print(isinstance(student1, Students))
print(issubclass(Students, UniversityPeople))