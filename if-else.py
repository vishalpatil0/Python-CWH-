#greatr than 

var1=int(input("enter the first number = "))
var2=int(input("enter the second number = "))
var3=int(input("enter the third number = "))

if var1>var2:
    if var1>var3:
        print(var1," is greater number")
    else:
        print(var3," is greater number")
elif var2>var3:
    print(var2," is greater number")
else:
    print(var3," is greater number")

var1=12
var2=(12==var1)
print(var2)

l=[1,2,3,4]
if 2 in l:
    print("yes it is int the list")
print(2 in l)
print(2 not in l)

age=int(input("enter your age here"))

if age<18:
    print("no")
elif age==18:
    print("come here")
elif age>100 and age<7:
    print("please enter valid age")
else:
    print("you can drive")
