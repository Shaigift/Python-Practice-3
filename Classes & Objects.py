class student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation




## import from refers to student class
from student import student
student1 = student("Jim", "Business", 3.1, False)
print(student1.name)

