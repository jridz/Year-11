from abc import ABC, abstractmethod  # abc is the 'abstract base class' module
import math


# Create abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
        # This method is abstract and will be overridden in the subclasses

    @abstractmethod
    def perimeter(self):
        pass
        # This method is abstract and will be overridden in the subclasses

    @abstractmethod
    def sides(self):
        pass
        # This method is abstract and will be overridden in the subclasses

    def type(self):
        print("I am " + self.__class__.__name__ + " shape")


# create subclasses
class Circle(Shape):
    # init is in subclass, not superclass
    def __init__(self, radius):
        self.radius = radius

    # Calculate area with pi * r^2
    def area(self):
        area = math.pi * self.radius * self.radius
        print("My area is " + str(area))

    # Calculate perimeter with 2 * pi * r
    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print("My perimeter is " + str(perimeter))

    # Print number of sides, none since it's a circle
    def sides(self):
        print("I have no sides")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.num_sides = 4

    # Calculate area with length * width
    def area(self):
        area = self.length * self.width
        print("My area is " + str(area))

    # Calculate perimeter with 2 * (length + width)
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print("My perimeter is " + str(perimeter))

    # Print number of sides from num_sides
    def sides(self):
        print("I have" + str(self.num_sides) + "sides")


# Declare shapes
circle1 = Circle(5)
rectangle1 = Rectangle(5, 10)

# Call circle's methods
circle1.area()
circle1.perimeter()

# Call rectangle's methods
rectangle1.area()
rectangle1.perimeter()
