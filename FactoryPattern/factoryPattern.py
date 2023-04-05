from abc import ABC, abstractmethod


class Shape(ABC):
    def draw(self):
        print("Drawing the Shape")


class Circle(Shape):
    def draw(self):
        print("Drawing circle")


class Square(Shape):
    def draw(self):
        print("Drawing Square")


class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")


class ShapeFactory:
    def __init__(self):
        print("ShapeFactory Object Created")

    def getShape(self, input):

        if input.lower() == "circle":
            return Circle()
        elif input.lower() == "square":
            return Square()
        elif input.lower() == "rectangle":
            return Rectangle()
        else:
            return None


s1 = ShapeFactory()
s1.getShape("ad").draw()
