'''
Created on May 13, 2013
@author: tnguyen7

Corrected on May 16, 2013
x Pass arguments to adder as a tuple: self.assertRaises(TypeError, adder, ("123", "456"))
o Pass individual arguments to adder: self.assertRaises(TypeError, adder, "123", "456")
'''
import unittest
from adder import adder

class Test(unittest.TestCase):

    def test_adder_errors(self):
        "Tests ensuring errors in data that cause TypeError raises."
        self.assertRaises(TypeError, adder, "123", "456")
        self.assertRaises(TypeError, adder, "123", 456)
        self.assertRaises(TypeError, adder, "123", 456)
        self.assertRaises(TypeError, adder, 1.23, 456)
    
    def test_adder_successes(self):
        "Tests ensuring that valid data passes."
        self.assertTrue(adder(1, 2) == 3, "1 + 2 is not 3")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_adder_errors', 'Test.test_adder_succusses']
    unittest.main()
