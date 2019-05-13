import unittest
from Week2.Utility_ds.utilitis import BinarySearchTree

class Binary_Tree(unittest.TestCase):
    def test_test_binary_tree(self):
        logic_obj = BinarySearchTree()  # creating the object of method class
        result = logic_obj.count(3)
        excepted = 5
        self.assertTrue(result, excepted)

if __name__ == '__main__':
    unittest.main()