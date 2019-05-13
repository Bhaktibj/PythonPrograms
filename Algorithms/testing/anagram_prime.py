import unittest
from Week1.Algorithms import utility

class Anagram_Prime(unittest.TestCase):
    def test_anagram_prime(self):
        result = utility.anagram_prime()
        excepted = True
        self.assertTrue(result, excepted)

if __name__ == '__main__':
    unittest.main()