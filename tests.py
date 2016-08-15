#!/usr/bin/env python3
import unittest
# I need to put my code in a class in order to be able to import it

class OutcomesTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()