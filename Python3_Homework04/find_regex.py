'''
Created on 2013/05/21

@author: tnguyen7
'''
import re

class FindRegex:
    
    def __init__(self, pat, text):
        """
        Find the position of a search string in a text.
        Return a tuple containing the start and the end position of the search string. 
        """
        m = re.search(pat, text)
        self.result = m.span()
