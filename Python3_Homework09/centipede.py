'''
Created on May 30, 2013

@author: tnguyen7
'''
class Centipede:
    def __init__(self):
        self.__dict__['stomach'] = []
        self.__dict__['legs'] = []
    
    def __call__(self, *args):
        self.__dict__['stomach'].extend(args)

    def __setattr__(self, key, value):
        "Protect the 'legs' and 'stomach' attributes against having their values reset from outside"
        if key in ('stomach', 'legs'):
            raise AttributeError("{0} is for internal use only".format(key))
        self.legs.extend([key])
        self.__dict__[key] = value
    
    def __str__(self):
        return ",".join(self.stomach)
    
    def __repr__(self):
        return ",".join(self.legs)
