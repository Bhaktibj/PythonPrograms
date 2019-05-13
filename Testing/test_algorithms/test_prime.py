import unittest
from Week1.Algorithms import utility

class Check_Prime(unittest.TestCase):
    def test_check_prime(self):
        result = utility.check_prime(13)
        expected = True
        self.assertTrue(expected, result)


if __name__ == '__main__':
    unittest.main()
