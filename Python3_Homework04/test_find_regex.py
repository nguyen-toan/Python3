'''
Created on 2013/05/21

@author: tnguyen7
'''
import unittest
from find_regex import FindRegex

class TestFindRegex(unittest.TestCase):

    def test_find_regex(self):
        """
        Test assuring the position of the phrase "Regular Expressions" in the following text is 231 as the start and 250 as the end.
        """
        text  = 'In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory\n'
        text += 'in a set of models using a notation called "regular sets" as a method to do pattern matching. Active\n'
        text += 'usage of this system, called Regular Expressions, started in the 1960s and continued under such \n' 
        text += 'pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer.'
        pat   = 'Regular Expressions'
        f     = FindRegex(pat, text)
        self.assertEqual(f.result, (231, 250), "Matching positions are %s but (231, 250) is expected" % str(f.result))

if __name__ == "__main__":
    unittest.main()
