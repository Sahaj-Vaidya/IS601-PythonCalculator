import unittest
from Calculator import Calculator


class CalculatorTest(unittest.TestCase):
    calculator = Calculator()

    def test_add(self):
        self.assertEqual(4, self.calculator.add(2, 2))
        self.assertEqual(3.2, self.calculator.add(1, 2.2))

    def test_minus(self):
        self.assertEqual(2, self.calculator.minus(3, 1))
        self.assertEqual(-2, self.calculator.minus(1, 3))

    def test_multiple(self):
        self.assertEqual(12, self.calculator.multiple(3, 4))
        self.assertEqual(13.5, self.calculator.multiple(3, 4.5))

    def test_divide(self):
        self.assertEqual(3, self.calculator.divide(9, 3))

    def test_square(self):
        self.assertEqual(16, self.calculator.square(4))

    def test_root(self):
        self.assertEqual(5, self.calculator.squareroot(25, 5))

    def test_seven(self):
        self.assertEqual(18, self.calculator.multiple(9, 2))

    def test_eight(self):
        self.assertEqual(625, self.calculator.square(25))


if __name__ == "__main__":
    unittest.main()
