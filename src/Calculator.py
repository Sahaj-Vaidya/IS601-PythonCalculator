import math
number_types = (int, float, complex)


class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def minus(self, x, y):
        return x - y

    def multiple(self, x, y):
        return x * y

    def divide(self, x, y):
        return x/y

    def square(self, x):
        return x ^ 2

    def squareroot(self, x , y):
        return math.sqrt(x , y)