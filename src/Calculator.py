import math

number_types = (int, float, complex)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, x, y):
        self.result = float(x) + float(y)
        return self.result

    def minus(self, x, y):
        self.result = float(x) - float(y)
        return self.result

    def multiple(self, x, y):
        self.result = float(x) * float(y)
        return self.result

    def divide(self, x, y):
        self.result = float(x) / float(y)
        return self.result

    def square(self, x):
        self.result = float(x) ** 2
        return self.result

    def squareroot(self, x):
        self.result = math.sqrt(float(x))
        return self.result

    def getLength(self, a):
        return len(a)