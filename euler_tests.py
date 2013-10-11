# euler_test.py
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

import inspect
import unittest
import nose

import euler002

# -----------------


class Check_eulers(unittest.TestCase):  
      
        def test_e2(self):  
            self.assertEqual(euler002.e2(),4613732)  
      
def eulertests():  
        print '####################'  
        print 'testing file', inspect.currentframe().f_code.co_filename   # filename  
        suite = unittest.TestLoader().loadTestsFromTestCase(Check_eulers)  
        unittest.TextTestRunner(verbosity=2).run(suite)  
       


if __name__ == '__main__': 
    eulertests()  
