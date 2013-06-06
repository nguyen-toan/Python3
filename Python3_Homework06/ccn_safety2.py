'''
Created on 2013/05/21

@author: tnguyen7
'''
import re

class CcnSafety2():
    
    def __init__(self, text):
        """
        Uses a compiled regular expression to replace the credit card numbers with "CCN REMOVED FOR YOUR SAFETY"
        """ 
        regex = re.compile(r"""
            \d{4}-   # first 4 digits of a credit card and a hyphen
            \d{4}-   # second 4 digits of a credit card and a hyphen
            \d{4}-   # third 4 digits of a credit card and a hyphen
            \d{4}    # last 4 digits of a credit card
            """, re.VERBOSE)
        self.result = regex.sub("CCN REMOVED FOR YOUR SAFETY", text)
    
    def __str__(self):
        "Returns the updated string"
        return self.result
