# euler003.py
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

import math
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def isprime(p):
    """
    Checks if n is prime by one iteration of Fermat's little theorem.
    (not used slow for large numbers)
    """
    a = 2 # any integer
    r = ((a ** p) - a) % p
    if r == 0:
        return True
    else:
        return False

def e3(i):
    possible_primes = get_primes (int(math.sqrt(i)))
    possible_primes.reverse()
    for possible_prime in possible_primes:
        if i % possible_prime == 0:
            return possible_prime
    print possible_primes
    
# -----------------

def test():
    rtn = e3(13195)
    assert(rtn == 29 )
    print rtn
    rtn = e3(600851475143)
    assert(rtn == 6857 )
    print rtn

if __name__ == '__main__':
    test()
