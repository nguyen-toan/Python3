'''
Created on 2013/05/21

@author: tnguyen7
'''
import re

class CcnSafety():
    
    def __init__(self, text):
        "Substitutes X for all but the last four digits of any credit card numbers." 
        pat = "\d{4}-\d{4}-\d{4}"
        self.result = re.sub(pat, "XXXX-XXXX-XXXX", text)
    
    def __str__(self):
        "Returns the updated string"
        return self.result
