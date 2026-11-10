import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,3),4)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(-2,-2),-4)


    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(4,3),1)
        self.assertEqual(subtract(-1,-2),-3)
        self.assertEqual(subtract(-1,1),0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEquals(mul(3, 2), 6)
        self.assertEquals(mul(2, 4), 8)
        self.assertEquals(mul(1, 5), 5)


    def test_divide(self): # 3 assertions
        self.assertEquals(div(2, 4), 2)
        self.assertEquals(div(3, 12), 4)
        self.assertEquals(div(1, 6), 6)

    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEqual(logarithm(10,1),0)
        self.assertEqual(logarithm(-10,100),2)
        self.assertEqual(logarithm(10,100),2)
    def test_log_invalid_base(self): # 1 assertion
        with self.assetRaises(ValueError):
            logarithm(10,0)
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuese(3, 4), 5)
        self.assertAlmostEqual(hypotenuese(5, 12), 13)
        self.assertAlmostEqual(hypotenuese(1, 2), math.sqrt(5))


    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(5)
            square_root(3)
            square_root(8)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()