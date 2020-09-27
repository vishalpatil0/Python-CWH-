#divide by zero exception

a=int(input("enter the 1st number = "))
b=int(input("enter the 2nd number = "))

try:
    print(a/b)
except Exception as e:
    print(e)