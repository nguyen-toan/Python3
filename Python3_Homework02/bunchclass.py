"""
Simple bunch class with a pretty printing method that protects its API.
"""

import unittest

class Bunch(object):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                raise AttributeError("API conflict: '%s' is part of the '%s' API" % (key, self.__class__.__name__))
            else:
                setattr(self, key, value)
    
    def pretty(self):
        text = ""
        for key, value in self.__dict__.items():
            text += "%s: %s\n" % (key, value)
        return text

class TestBunch(unittest.TestCase):
    
    def test_pretty(self):
        self.assertRaises(AttributeError, Bunch, name="Audrey", job="Software Developer", pretty=True)
        b = Bunch(name="Audrey", job="Software Developer")
        p = b.pretty()
        self.assertTrue("Audrey" in p)
        self.assertFalse("pretty: True" in p)

if __name__ == "__main__":
    unittest.main()
