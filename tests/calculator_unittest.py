import unittest
from calculator import Calculator


class CalculatorUnitTests(unittest.TestCase):

    def __init__(self):
        super(CalculatorUnitTests, self).__init__()
        self.calc = Calculator()

    def test_GIVEN_calculater_WHEN_set_number_called_THEN_number_is_correct(self):
        expected_output = 5
        self.calc.set_number(expected_output)
        self.assertEqual(self.calc.get_number(), expected_output)

