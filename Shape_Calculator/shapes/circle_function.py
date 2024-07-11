# shapes/circle.py

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return math.pi * self.radius ** 2

    def circle_circumference(self):
        return 2 * math.pi * self.radius
