# euler001.py
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def e1(n):
    rtn = 0
    for r in range(n):
       if r%3 == 0:
           rtn += r
       elif r%5 == 0:
           rtn += r
    return rtn
    
# -----------------

def test():
    rtn = e1(10)
    print rtn
    rtn = e1(1000)
    print rtn
test()

