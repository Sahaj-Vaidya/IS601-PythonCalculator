import unittest
from Calculator import Calculator
from CSVReader import CSVReader


class CalculatorTest(unittest.TestCase):
    calculator = Calculator()

    def test_subtraction(self):
        test_data = CSVReader("Data/Unit Test Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.minus(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_addition(self):
        test_data = CSVReader("Data/Unit Test Addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply(self):
        test_data = CSVReader("Data/Unit Test Multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiple(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide(self):
        test_data = CSVReader("Data/Unit Test Division.csv").data
        for row in test_data:
            len1 = self.calculator.getLength(row['Result'])
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2'], len1), result)
            self.assertEqual(self.calculator.result, result)

    def test_square(self):
        test_data = CSVReader("Data/Unit Test Square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_root(self):
        test_data = CSVReader("Data/Unit Test Square Root.csv").data
        for row in test_data:
            len1 = self.calculator.getLength(row['Result'])
            result = float(row['Result'])
            self.assertEqual(self.calculator.squareroot(row['Value 1'], len1), result)
            self.assertEqual(self.calculator.result, result)

    def test_add(self):
        self.assertEqual(4, self.calculator.add(2, 2))
        self.assertEqual(3.2, self.calculator.add(1, 2.2))

    def test_minus(self):
        self.assertEqual(2, self.calculator.minus(3, 1))
        self.assertEqual(-2, self.calculator.minus(1, 3))

    def test_multiple(self):
        self.assertEqual(12, self.calculator.multiple(3, 4))
        self.assertEqual(13.5, self.calculator.multiple(3, 4.5))

    def test_division(self):
        self.assertEqual(3, self.calculator.divide(9, 3))

    def test_squares(self):
        self.assertEqual(16, self.calculator.square(4))

    def test_sqroot(self):
        self.assertEqual(5, self.calculator.squareroot(25))

    def test_seven(self):
        self.assertEqual(18, self.calculator.multiple(9, 2))

    def test_eight(self):
        self.assertEqual(625, self.calculator.square(25))


if __name__ == "__main__":
    unittest.main()
