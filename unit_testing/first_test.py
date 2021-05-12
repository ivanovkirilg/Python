'''
Created on May 12, 2021

@author: kivag
'''

import unittest

class NumEqualityTest(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1, 1.0)

    def test_int_str(self):
        self.assertEqual(1, '1')

if __name__ == '__main__':
    unittest.main()

