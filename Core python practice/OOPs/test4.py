class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.widtgh = width
    def area(self):
        return self.height*self.widtgh
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2

def result(i):
    print(i.area())

jill = Rectangle(2,3)
tim = Circle(2)

result(jill)
result(tim)
