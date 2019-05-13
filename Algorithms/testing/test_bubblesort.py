import unittest
from Week1.Algorithms import utility

class Bubble_Sort(unittest.TestCase):
    def test_bubble_sort_with_positive_numbers(self):
        result =(utility.bubble_sort([ 5, 7, 8, 2, 4, 1 ]),
                         [ 1, 2, 4, 5, 7, 8 ])
        excepted = True
        self.assertTrue(excepted, result)

if __name__ == '__main__':
    unittest.main()