'''
Created on May 17, 2013

@author: tnguyen7

Corrected on May 21, 2013
x This tries to get an attribute of the Inventory.add_count method called "South Asian", which that method does not have: self.assertRaises(AttributeError, getattr, Inventory.add_coconut, "South Asian")
o Create an instance (ex: inv = Inventory()) of an inventory with its own list for coconuts and check the return value of inv.add_coconut: self.assertRaises(AttributeError, inv.add_coconut, "South Asian")
'''
import unittest
from coconuts import Coconut, Inventory

class TestCoconut(unittest.TestCase):
    
    def test_coconut_type(self):
        """
        Tests ensuring different coconut types each have a different weight. 
        """
        south_asian_coconut    = Coconut("South Asian")
        middle_eastern_coconut = Coconut("Middle Eastern")
        american_coconut       = Coconut("American")
        self.assertNotEqual(south_asian_coconut.weight, middle_eastern_coconut.weight, "South Asian and Middle Eastern coconuts have the same weight")
        self.assertNotEqual(south_asian_coconut.weight, american_coconut.weight, "South Asian and American coconuts have the same weight")
        self.assertNotEqual(middle_eastern_coconut.weight, american_coconut.weight, "Middle Eastern and Middle Eastern coconuts have the same weight")
    
    def test_inventory_attribute(self):
        """
        Test ensuring if a string object is passed to the Inventory.add_coconut method, an AttributeError is thrown. 
        """
        inv = Inventory()
        self.assertRaises(AttributeError, inv.add_coconut, "South Asian")
    
    def test_inventory_total_weight(self):
        """
        Test ensuring if 2 South Asian, 1 Middle Eastern, and 3 American coconuts are added to the inventory, 
        the Inventory.total_weight() method returns 19.
        """
        south_asian_coconut    = Coconut("South Asian")
        middle_eastern_coconut = Coconut("Middle Eastern")
        american_coconut       = Coconut("American")

        inventory = Inventory()
        inventory.add_coconut(south_asian_coconut)
        inventory.add_coconut(south_asian_coconut)
        inventory.add_coconut(middle_eastern_coconut)
        inventory.add_coconut(american_coconut)
        inventory.add_coconut(american_coconut)
        inventory.add_coconut(american_coconut)
        
        self.assertEqual(inventory.total_weight(), 19, "Total weight of coconuts is %f but 19 is expected." % inventory.total_weight())
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_coconut_type']
    unittest.main()
