import math

class Geometric:
    def area(self):
        raise NotImplementedError("Метод площади должен быть переопределен в дочерних классах")


class Rectangle(Geometric):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Circle(Geometric):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r**2


class Rhombus(Geometric):
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def area(self):
        return 0.5 * self.d1 * self.d2


# Примеры использования
rectangle = Rectangle(4, 6)
print(f"Площадь прямоугольника: {rectangle.area()}")

circle = Circle(8)
print(f"Площадь круга: {circle.area()}")

rhombus = Rhombus(4, 6)
print(f"Площадь ромба: {rhombus.area()}")