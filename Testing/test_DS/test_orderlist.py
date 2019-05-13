import unittest
from Week2.Utility_ds.utilitis import OrderedList

class Order_List(unittest.TestCase):
    def test_order_list(self):
        logic_obj = OrderedList()  # creating the object of method class
        result = logic_obj.search_item(2)
        excepted = True
        self.assertTrue(result, excepted)

if __name__ == '__main__':
    unittest.main()