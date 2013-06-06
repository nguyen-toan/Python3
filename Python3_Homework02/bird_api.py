"""
API for software birds carrying objects.
"""
from bunchclass import Bunch

class Bird(Bunch):
    
    def pretty(self):
        """
        Replacement pretty() method
        """
        return "pretty bird!"
        
    def add(self, name, value):
        """
        Add an object for the Bird to carry in its basket.
            Name is a string naming the object
            Value is the actual object being placed in the basket.
        """
        if hasattr(self, name):
            raise KeyError("'%s' object cannot be placed in basket")
        else:
            setattr(self, name, value)
        
    def remove(self, name):
        """
        Calculate the speed of the bird.
            algorithm: 100 - (5*number of objects in the basket)
            result cannot be less than zero.
        """
        if name in self.__dict__:
            delattr(self, name)
        else:
            raise KeyError("'%s' object not found in basket")
    
    def calculate(self):
        """
        Calculate the speed of the bird.
            algorithm: 100 - (5*number of objects in the basket)
            result cannot be less than zero.
        """
        return max(100 - len(self.__dict__) * 10, 0)
        
    def basket(self):
        """
        Print in an attractive format the list of objects in the basket.
        """
        return "Basket Objects\n" + self.pretty()

if __name__ == "__main__":
    swallow = Bird(fruit=("coconut", "orange"), drink="apple juice")
    swallow.add("cars", 3)
    print(swallow.basket())
    print(swallow.calculate())
    swallow.remove("drink")
    print(swallow.basket())
    print(swallow.calculate())
#    help(swallow)
