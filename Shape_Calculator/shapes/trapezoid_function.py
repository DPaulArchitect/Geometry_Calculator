# shapes/trapezoid.py

class Trapezoid:
    def __init__(self, base1, base2, side1, side2, height):
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2
        self.height = height

    def trapezoid_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def trapezoid_perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2
