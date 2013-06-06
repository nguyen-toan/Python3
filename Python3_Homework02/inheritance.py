"""
Complex inheritance program
"""

class Maurice(object):
    def hair(self):
        return "red"

class Vivian(object):
    def hair(self):
        return "brown"

class Isadore(object):
    def hair(self):
        return "bald"
    
class Tracy(object):
    def hair(self):
        return "gray"

class Mother(Maurice, Vivian):
    pass

class Father(Isadore, Tracy):
    pass

class Child(Father, Mother):
    pass

if __name__ == "__main__":
    child = Child()
    print(child.hair())
