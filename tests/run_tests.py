import unittest
import sys
import xmlrunner


def run_all_tests():

    suite = unittest.TestLoader().discover(".", pattern="*test.py")
    result = xmlrunner.XMLTestRunner(output="test-reports").run(suite).wasSuccessful()
    return result


def main():

    success = run_all_tests()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
