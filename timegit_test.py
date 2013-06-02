# timegit_test

import time
import euler001




def run001(): 
    euler001.e1(1000)

def run():
    run001()
   
if __name__ == '__main__':
    s = time.time()
    run()
    print 'took ', time.time() -s 
