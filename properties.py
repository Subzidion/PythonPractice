import math

class Square:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        """Area of square."""
        return self.side ** 2

    @area.setter
    def area(self, value):
        self.side = math.sqrt(value)

    @area.deleter
    def area(self):
        print("You cannot delete this property.")
