# programming_paradigm/test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(2.5, 1.0), 1.5)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero

    def test_division_by_zero(self):
        """Explicit test for division by zero."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))  # Edge case: 0/0 is undefined

if __name__ == '__main__':
    unittest.main()
