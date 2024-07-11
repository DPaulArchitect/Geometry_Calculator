# shapes/ellipse.py

import math


class Ellipse:
    def __init__(self, semi_major_axis, semi_minor_axis):
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

    def ellipse_area(self):
        return math.pi * self.semi_major_axis * self.semi_minor_axis
