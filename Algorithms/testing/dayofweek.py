import unittest
from Week1.Algorithms import utility


class Check_Anagram(unittest.TestCase):
    def test_anagram_str(self):
        result = utility.day_of_week(1,1,2001)
        expected = 'monday'
        self.assertTrue(expected,result)

if __name__ == '__main__':
    unittest.main()