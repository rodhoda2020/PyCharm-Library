class Student:
    def __init__(self):
        self.name = 'Rolf'
        self.grade = (90, 90, 93, 78, 90)

    def average(self):
        return sum(self.grade) / len(self.grade)


student = Student()
print(student.name)
print(student.grade)
print(student.average())