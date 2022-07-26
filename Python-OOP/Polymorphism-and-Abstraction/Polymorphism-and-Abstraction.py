class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()


# ---------------------------------------------------------------------------------------

def start_playing(guitar):
    return guitar.play()


# ---------------------------------------------------------------------------------------

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape, ABC):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return pi * (self.__radius ** 2)

    def calculate_perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape, ABC):
    def __init__(self, height, width):
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)
