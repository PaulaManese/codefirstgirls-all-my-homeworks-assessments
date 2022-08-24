from number3anspalindrome import *

import unittest

class TestPalindrome(unittest.TestCase):
    # Supplied a valid palindrome word
    def testSucces(self):
        self.assertIn("It is a palindrome", isPalindrome("madam"))
    
    # Supplied a valid palindrome word but the casing is different, this should still return true because I used .toLower()
    def testUppercase(self):
        self.assertIn("It is a palindrome", isPalindrome("Madam"))
    
    # Supplied an invalid palindrome
    def testFailed(self):
        self.assertIn("It is not a palindrome", isPalindrome("Pao"))


# python -m unittest test_palindrome.py  
