# shapes/rectangle_function.py

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_perimeter(self):
        return 2*(self.length + self.width)

    def rectangle_area(self):
        return self.length * self.width
