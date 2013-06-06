'''
Created on May 28, 2013

@author: tnguyen7
'''
class Furnishing:
    def __init__(self, room):
        self.room = room

class Sofa(Furnishing):
    pass

class Bookshelf(Furnishing):
    pass

class Bed(Furnishing):
    pass
    
class Table(Furnishing):
    pass

def map_the_home(home):
    """
    Convert a furniture object list to a built-in dict type where the rooms are the individual keys 
    and the associated value is the list of furniture for that room
    """
    res = {}
    for obj in home:
        room = obj.room
        if room in res:
            res[room].append(obj)
        else:
            res[room] = [obj]
    return res
    
def counter(home):
    """
    Prints the types of furniture and how many there are of each type. 
    """
    res_dict = {'Bed'      : ['Beds'       , 0], 
                'Bookshelf': ['Bookshelves', 0], 
                'Sofa'     : ['Sofas'      , 0], 
                'Table'    : ['Tables'     , 0]}
    
    for obj in home:
        res_dict[obj.__class__.__name__][1] += 1
    
    for value in res_dict.values():
        print("%s: %d" % (value[0], value[1]))
        
if __name__ == "__main__":
    home = []
    home.append(Bed('Bedroom'))
    home.append(Sofa('Living Room'))
    print(map_the_home(home))
    counter(home)
