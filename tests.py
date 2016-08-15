#!/usr/bin/env python3
import unittest
# I need to put my code in a class in order to be able to import it

class OutcomesTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_syntax_check(self):
        self.assertTrue(syntax_check("http://google.com"))

    # test CSV of URLs:
    # http://google.com, http, http:///someurl.com, http://asdfasdfasdfasdfasdfasd.com, http://google.com/bad

    # HIT TIME LIMIT
    # I believe that testing is EXTREMELY important, but I did not have time to learn how to test in python.
    # Ultimately I would have liked to test each function used in validator.

if __name__ == '__main__':
    unittest.main()