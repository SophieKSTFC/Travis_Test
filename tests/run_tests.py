import unittest
import sys

from calculator_unittest import CalculatorUnitTests

def run_all_tests():
    suite = unittest.TestLoader().discover(".", pattern="*test.py")

    runner = unittest.TextTestRunner()
    return runner.run(suite)

def main():

    success = run_all_tests()
    print success
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()