from os import name,system as sys
def clear():
    if name=='nt':  # for windows 
        sys('cls')
    elif name=='posix':
        sys('clear')
