import unittest
from Week1.Algorithms import utility


class Check_Binary(unittest.TestCase):
    def test_to_binary(self):
        result = utility.to_binary(2)
        expected ='10'
        self.assertTrue(result,expected)

if __name__ == '__main__':
    unittest.main()