#greatr than 

var1=int(input("enter the first number = "))
var2=int(input("enter the second number = "))
var3=int(input("enter the third number = "))

if var1>var2 and var1>var3:
    print(var1," is greater number")
elif var2>var1 and var2>var3:
    print(var2," is greater number")
else:
    print(var3,"is greater number")


#short hand if else notation 

if var1>var2: print("a is greater thatn b")

print("a is greater than b") if(var1<var2) else print('b is greater than b')