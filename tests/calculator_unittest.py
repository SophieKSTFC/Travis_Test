import unittest


class CalculatorUnitTests(unittest.TestCase):

   def test_GIVEN_no_test_THEN_return_failure(self):
       self.assertEqual(True, False)
       