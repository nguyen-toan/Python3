class Coconut(object):
    
    "Coconut dictionary: each coconut has a type and a weight"
    coconut_dict = {"South Asian" : 3,
                    "Middle Eastern" : 2.5,
                    "American" : 3.5
                    }

    def __init__(self, coconut_type):
        """
        Accept an argument string to create a coconut object.
        The argument string must be in the coconut dictionary, otherwise the AttributeError is thrown.
        """
        if coconut_type in Coconut.coconut_dict.keys():
            self.type   = coconut_type
            self.weight = Coconut.coconut_dict[coconut_type]
        else:
            raise AttributeError("'%s' is not in the coconut dictionary." % coconut_type)                      
 
class Inventory(object):
    
    def __init__(self):
        self.inventory = []
    
    def add_coconut(self, coconut):
        """
        Add a coconut to the inventory. Throw an AttributeError if the argument is not a coconut object. 
        """
        if not isinstance(coconut, Coconut):
            raise AttributeError("Input must be a 'Coconut', not a '%s' object" % coconut.__class__.__name__)
        self.inventory.append(coconut)
    
    def total_weight(self):
        """
        Calculate the total weight of coconuts.
        """
        total_weight = 0
        for coconut in self.inventory:
            total_weight += coconut.weight
        return total_weight
