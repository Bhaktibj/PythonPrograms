import unittest
from Week1.Algorithms import utility

class Temperature(unittest.TestCase):

    def test_temp(self):
        result = utility.temp_conversion(2)
        excepted = (35.6, 17.822222222222223)
        self.assertAlmostEqual(result,excepted)

if __name__ == '__main__':
    unittest.main()