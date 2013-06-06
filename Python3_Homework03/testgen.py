"""
testgen.py: simple test for a sequence generator
"""
import unittest
from class123 import gen123

class TestGen(unittest.TestCase):
    
    def testEmpty(self):
        self.assertEqual(list(gen123([])), [], "Empty list does not give empty list")
    
    def test123(self):
        self.assertEqual(list(gen123([1])), [1], "[1] does not give [1]")
        self.assertEqual(list(gen123([1, 2])), [1, 2, 2])
        self.assertEqual(list(gen123([1, 2, 3])), [1, 2, 2, 3, 3, 3])

if __name__ == "__main__":
    unittest.main()
