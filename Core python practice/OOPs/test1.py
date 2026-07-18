class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}"

s1 = Student("Jill",20,"A+")
print(str(s1))