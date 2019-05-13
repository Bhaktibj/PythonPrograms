import unittest
from Week1.Algorithms import utility


class Check_Anagram(unittest.TestCase):
    def test_anagram_str(self):
        result = utility.sqrt_root(4)
        expected = 2.0
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()