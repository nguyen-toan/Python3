'''
Created on May 14, 2013

Inheritance test program

@author: tnguyen7
'''

import unittest
from inhairitance import Child

class TestHair(unittest.TestCase):
    
    def test_hair(self):
        child = Child()
        hair = child.hair()
        self.assertNotEqual(hair, "red")
        self.assertNotEqual(hair, "brown")        
        self.assertNotEqual(hair, "gray")
        self.assertEqual(hair, "bald")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_hair']
    unittest.main()
