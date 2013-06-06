"""
Simple demonstration of the "old iteration protocol" - still available.
"""
class fls(object):
    def __init__(self, val, times):
        self.val = val
        self.count = times
    
    def __getitem__(self, n):
        if n >= self.count:
            raise IndexError("Object has no item %s %n")
        return self.val

thing = fls("*", 5)
for c in thing:
    print(c)

thing = fls(120, 3)
for c in thing:
    print(c)
