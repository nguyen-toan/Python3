import unittest
from property_address import *
   
class TestAddresses(unittest.TestCase): 
   
    def setUp(self): 
        self.home = Address( name='Steve Holden', street_address='1972 Flying Circus', city='Arlington', state='NYK', zip_code='12345-6789' )
       
    def test_name(self):
        self.assertEqual(self.home.name, 'Steve Holden') 
        self.assertRaises(AttributeError, setattr, self.home, 'name', 'Daniel Greenfeld')
        
    def test_state(self): 
        self.assertEqual(self.home.state, 'NYK') 
        self.assertRaises(StateError, setattr, self.home, 'state', 'NY')  
        self.home.state = 'ABC' 
        self.assertEqual(self.home.state, 'ABC')  
        
    def test_zip_code(self): 
        self.assertEqual(self.home.zip_code, '12345-6789') 
        self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', '12345')
        self.home.zip_code = '54321-9876' 
        self.assertEqual(self.home.zip_code, '54321-9876') 
       
if __name__ == "__main__":
    start_logging(level="INFO")
    unittest.main()
