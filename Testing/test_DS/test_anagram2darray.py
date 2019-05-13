import unittest
from Week2.Utility_ds.utilitis import Methods

class Anagram_Two_Array(unittest.TestCase):
    def test_anagram_2d_array(self):
        logic_obj = Methods()  # creating the object of method class
        result = logic_obj.anagram_2d_array(self)
        excepted = True
        if ValueError:
            self.assertFalse(result)
        else:
            self.assertTrue(result, excepted)

if __name__ == '__main__':
    unittest.main()