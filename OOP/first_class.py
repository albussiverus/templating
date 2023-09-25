
class MyFirstClass:
    """MyFirstClass - вчимося створювати класи"""
    pass

class Student:
    name = "NoName"
    age = 0
    scores = []

tom = Student()
john = Student()

print(tom.name)

john.name = "John"
print(Student.name, john.name, tom.name)
Student.name = "Marina"

print(Student.name, john.name, john.age, tom.name)








