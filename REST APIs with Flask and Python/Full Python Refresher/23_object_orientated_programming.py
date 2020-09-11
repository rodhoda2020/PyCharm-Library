class Student:

    # This is the constructor where we will initialize the variables of the class
    def __init__(self, name, grades):
        self.name = name
        self.grade = grades

    def average(self):
        return sum(self.grade) / len(self.grade)


# This is how you would send the arguments to the class
student = Student('Bob', (100, 100, 93, 87, 90))
student2 = Student('Chad', (99, 99, 93, 92, 83))
print(student.name)
print(student.grade)
print(student.average())
print(student2.average())
