from os import name,system as sys
import time
def clear():
    if name=='nt':  # for windows 
        sys('cls')
    elif name=='posix':
        sys('clear')
if __name__=="__main__": 
    print("before clear")
    time.sleep(2)
    clear()
    print("clearing")
    time.sleep(2)
    clear()       
    print("after  clear")