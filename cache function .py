"""
NOTE:
        lru_cache function only stores the output of the function of the recent calls
        it doesn't stores the print statement like operation 
        it only stores the return value from the function
"""
from os import system
import time
from functools import lru_cache as lrc
@lrc(maxsize=int(input("enter the maximum size of lar_cache")))
def somew(n):
    time.sleep(n)   #print function doesn't work in this module
    return n
if __name__ == "__main__":
    print(somew(2))
    print("calling again")
    # system('clear')
    input()
    print(somew(2))
    print("done second time")
    input()
    print(somew(2))
    print("third time")
    input()
    print(somew(4))
    print("fourth time")