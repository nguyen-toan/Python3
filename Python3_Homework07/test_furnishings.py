'''
Created on May 28, 2013

@author: tnguyen7
'''
import unittest
from furnishings import *

class TestFurnishings(unittest.TestCase):

    def test_map_the_home(self):
        home = []
        home.append(Bed('Bedroom'))
        home.append(Sofa('Living Room'))
        map_home = map_the_home(home)
        self.assertTrue(isinstance(map_home, dict), "map_the_home() return '%s' but dict type is expected" % type(map_home))
        self.assertTrue('Bedroom' in map_home, "Bedroom is expected to be listed")
        self.assertTrue('Living Room' in map_home, "Living Room is expected to be listed")
        self.assertTrue(isinstance(map_home['Bedroom'], list), "The value of 'Bedroom' is expected to be a list.")
        self.assertTrue(isinstance(map_home['Living Room'], list), "The value of 'Living Room' is expected to be a list.")
        
if __name__ == "__main__":
    unittest.main()
