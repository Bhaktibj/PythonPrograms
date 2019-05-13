import unittest
from Week1.Algorithms import utility


class Check_Anagram(unittest.TestCase):
    def test_anagram_str(self):
        result = utility.monthly_payment(10000,1,3)
        expected = 24.027091929939754
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()