print(sum((2,3)))

from multipledispatch import dispatch 
@dispatch(int,int)
def adder(a,b):
    return a+b

@dispatch(str)
def adder(s):
    print("this is normal function")

@dispatch(int,str)
def adder(a,b):
    print(a,b)

print(adder(3,4))

adder("s")

adder(1,"string")

