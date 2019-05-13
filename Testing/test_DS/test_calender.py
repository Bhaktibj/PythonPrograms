import unittest
from Week2.Utility_ds.utilitis import Cal_Methods

class Anagram_Two_Array(unittest.TestCase):
    def test_anagram_2d_array(self):
        logic_obj = Cal_Methods()
        # creating the object of method class
        result = logic_obj.calendar(2,2004)
        excepted = True
        self.assertTrue(result, excepted)

if __name__ == '__main__':
    unittest.main()