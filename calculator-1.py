#faulty calculator gives correct output except for 45*3 , 56/6 and 56+9
line1=" is = "
input1=input("Enter the operator = ")
var1=int(input("enter the first number = "))
var2=int(input("enter the second number = "))
if input1=='+':
    if var1==56 and var2==9:
        print(var1,"+",var2,"=77")
    else:
        print("Addition of ",var1,"+",var2,line1,var1+var2)
elif input1=='-':
    print("Substracion of ",var1,"-",var2,line1,var1-var2)
elif input1=='*':
    if var1==45 and var2==3:
        print(var1,"*",var2,"=555")
    else:
        print("Multipication of ",var1,"*",var2,line1,var1*var2)
elif input1=='/':
    if var1==56 and var2==6:
        print(var1,"/",var2,"=4")
    else:
        print("Division of ",var1,"/",var2,line1,var1/var2)
else:
    print("please eneter valid choice")
