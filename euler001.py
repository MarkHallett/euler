# euler001.py
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def e1(n):
    return sum(x for x in range(n) if x%3 == 0 or x%5 == 0)
    
# -----------------

def test():
    rtn = e1(10)
    print rtn
    assert(rtn == 23 )
    rtn = e1(1000)
    print rtn

if __name__ == '__main__':
    test()
