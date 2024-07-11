# shapes/parallelogram.py

class Parallelogram:
    def __init__(self, base, side, height):
        self.base = base
        self.side = side
        self.height = height

    def parallelogram_area(self):
        return self.base * self.height

    def parallelogram_perimeter(self):
        return 2 * (self.base + self.side)
