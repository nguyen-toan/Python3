'''
Created on 2013/05/21
@author: tnguyen7

Corrected on 2013/05/28
- A test to compare the whole text is added.
'''
import unittest
from ccn_safety2 import CcnSafety2

class TestCcnSafety2(unittest.TestCase):

    def test_ccn_safety2(self):
        """
        Test assuring all but the last four digits of any credit card numbers are substituted by X.
        """        
        text            = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts."
        expected_output = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY? It is because a number that appears to be real, such as CCN REMOVED FOR YOUR SAFETY, triggers the attention of privacy and security experts." 
        c = CcnSafety2(text)
        output = str(c)
        self.assertTrue("CCN REMOVED FOR YOUR SAFETY" in output, "Credit card numbers are not masked properly.")
        self.assertTrue("555-123-4567" in output, "Phone number should not be replaced.")
        self.assertEqual(output, expected_output, "The converted text is not expected.")

if __name__ == "__main__":
    unittest.main()
