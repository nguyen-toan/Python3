import unittest
from centipede import Centipede

class TestBug(unittest.TestCase):
    def test_stomach(self):
        ralph = Centipede()         
        ralph('chocolate')         
        ralph('bbq')
        ralph('cookies')
        ralph('salad')
        self.assertEqual(ralph.__str__(), 'chocolate,bbq,cookies,salad')
    
    def test_legs(self):
        ralph = Centipede()
        ralph.friends = ['Steve', 'Daniel', 'Guido']
        ralph.favorite_show = "Monty Python's Flying Circus"
        ralph.age = '31'
        self.assertEqual(ralph.age, '31', "ralph doesn't know how old he is")
        self.assertEqual(ralph.__repr__(), 'friends,favorite_show,age')
          
    def test_protected(self):
        ralph = Centipede()
        self.assertRaises(AttributeError, setattr, ralph, "legs", [])
        self.assertRaises(AttributeError, setattr, ralph, "stomach", [])
        
if __name__ == "__main__":
    unittest.main()
