a=input("enter your name here")

if a.isnumeric():
    raise Exception("Numbers are not allowed")

b=int(input("Enter the number"))

if b==0:
    raise ZeroDivisionError("B is zero")

raise TypeError("vihal")



