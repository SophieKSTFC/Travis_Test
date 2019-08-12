import unittest
import sys

from calculator_unittest import CalculatorUnitTests

def run_all_tests():

    suite = unittest.TestLoader().discover(".", pattern="*test.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return result.wasSuccessful():


def main():

    success = run_all_tests()
    
    sys.exit(0 if success else 1)
    #if not success:
        #raise Exception

if __name__ == "__main__":
    main()