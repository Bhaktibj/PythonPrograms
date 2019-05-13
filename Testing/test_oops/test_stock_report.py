import unittest
from Week3.ObjectOrientedProgramming.StockReport import StockData, StockValues

class Stock_Report(unittest.TestCase):
    def test_stock_report(self):
        obj = StockData # creating the object of method class
        result = obj.stock_data(self)
        excepted = True
        if ValueError:
            self.assertFalse(result,excepted)
        else:
            obj2 = StockValues
            result1 = obj2.stock_values(self)
            excepted = True
        self.assertTrue(result1, excepted)

if __name__ == '__main__':
    unittest.main()