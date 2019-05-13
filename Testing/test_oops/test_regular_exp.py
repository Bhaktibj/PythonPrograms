import unittest
from Week3.ObjectOrientedProgramming.Regular_Expression import RegularExpression

class Regular_Expression(unittest.TestCase):
    def test_regex(self):
        obj = RegularExpression # creating the object of method class
        result = obj.regex_function(self)
        excepted = True
        if ValueError:
            self.assertFalse(result,excepted)
        else:
            self.assertTrue(result, excepted)

if __name__ == '__main__':
    unittest.main()