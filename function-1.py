# a=12
# b=13
# c=sum((a,b))

def a(var1,var2):
    """this is a function for additon of two numbers"""  #this is a doc string means it give basic idea or descrive the work of function
    return var1+var2
    
print(a(23,23))

print(a.__doc__)   # function_name.__doc__ this syntax prints the doc string of function