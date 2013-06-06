'''
Created on 2013/05/21
@author: tnguyen7

Corrected on May 28, 2013
- A test to compare the whole text was added.
'''
import unittest
from ccn_safety import CcnSafety

class TestCcnSafety(unittest.TestCase):

    def test_ccn_safety(self):
        """
        Test assuring all but the last four digits of any credit card numbers are substituted by X.
        """        
        text            = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts."
        expected_output = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or XXXX-XXXX-XXXX-5555? It is because a number that appears to be real, such as XXXX-XXXX-XXXX-5678, triggers the attention of privacy and security experts."
        c = CcnSafety(text)
        output = str(c)
        self.assertTrue(("XXXX-XXXX-XXXX-5555" in output) and ("XXXX-XXXX-XXXX-5678" in output), 
                        "Credit card numbers are not masked properly.")
        self.assertTrue("555-123-4567" in output, 
                        "Phone number should not be replaced.")
        self.assertEqual(output, expected_output, "The converted output is not expected.")
        
if __name__ == "__main__":
    unittest.main()
