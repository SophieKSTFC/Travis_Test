import unittest
import sys
sys.path.append('../src/')
from calculator import Calculator

class CalculatorUnitTests(unittest.TestCase):

    calc = Calculator()

    def test_GIVEN_calculater_WHEN_set_number_called_THEN_number_is_correct(self):
        expected_output = 5
        self.calc.set_number(expected_output)
        self.assertEqual(self.calc.get_number(), expected_output)

