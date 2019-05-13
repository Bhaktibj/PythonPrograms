import unittest
from Week1.Algorithms import utility

# Test the given year is leap year or not.

class Check(unittest.TestCase):
    def test_check_leap(self):
        result = utility.check_Leap(2012)
        excepted = True
        self.assertTrue(excepted, result)

if __name__ == '__main__':
    unittest.main()