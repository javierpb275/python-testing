import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)


unittest.main()#This runs the entire test file

'''
Ran 1 test in 0.000s

OK
'''

'''
F
======================================================================
FAIL: test_do_stuff (__main__.TestMain)
----------------------------------------------------------------------
Traceback (most recent call last):
  File  "\python-testing\test.py", line 8, in test_do_stuff
    self.assertEqual(result, 10)
AssertionError: 15 != 10

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
'''