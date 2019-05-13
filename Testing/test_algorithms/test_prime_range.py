import unittest
from Week1.Algorithms import utility

class Prime_Range(unittest.TestCase):
    def test_prime_range(self):
        result = utility.prime_num()
        excepted = True
        self.assertTrue(result, excepted)

if __name__ == '__main__':
    unittest.main()