"""
A simple iterator object specification.
"""
class gen123:
    
    def __init__(self, lst):
        "Initialize the iterator object"
        self.lst = lst
        self.itemno = 0
        self.count = 1
        
    def __iter__(self):
        "This object is not an iterable"
        return self
    
    def __next__(self):
        "Return the next value in the output sequence."
        if self.count > self.itemno:
            try:
                self.val = self.lst[self.itemno]
            except IndexError:
                raise StopIteration
            self.itemno += 1
            self.count = 1
        self.count += 1
        return self.val
