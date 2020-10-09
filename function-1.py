# a=12
# b=13
# c=sum((a,b))

def a(var1,var2):
    """this is a function for additon of two numbers"""  #this is a doc string means it give basic idea or descrive the work of function
    return var1+var2
    
print(a(23,23))

print(a.__doc__)   # function_name.__doc__ this syntax prints the doc string of function


def func1(a):
    """we can also return function though a function 
    OR 
    in simple word we can also return function like we return arguments"""
    if a==1:
        return int
    elif a==0:
        return print
    
print(func1(1),"__doc__ of functinon=== \n\n",func1.__doc__)


def execut1(func1):
    """we can also pass function as arguments"""
    func1("this")

execut1(print)


def execut1(func1):
    """we can also pass function as arguments"""
    print(func1([5],6))

execut1(sum)