'''
adder.py: adds two objects if they are both of the integer type.
'''

def adder(x, y):
    """
    Return x + y if they are both integers
    """
    if not (isinstance(x, int) and isinstance(y, int)):
        raise TypeError("Inputs must be integers")
    return x + y
