class Circle:
    pi=3.14 # class variable
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        ar = Circle.pi*(self.radius**2)
        return ar

    def circumference(self):
        circum = 2*Circle.pi*(self.radius)
        return circum


# pi = 3.14
c1 = Circle(3)
print(c1.area())
print(c1.circumference())
