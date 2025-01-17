# shapes/square_function.py

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def square_perimeter(self):
        return 4 * self.side_length

    def square_area(self):
        return self.side_length ** 2
