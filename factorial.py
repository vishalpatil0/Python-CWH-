#factorial logic
#5=5!=5*4*3*2*1

#factorial of two numbers using recursion

# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)

# num1=int(input("Enter a number"))
# print("Factorial of ",num1," is = ",fact(num1))


#Factorial of a number using iteration


num1=int(input("Enter a number"))

fact=1
if (num1==0 or num1==1):
    print("FActorail is ",1)
else:
    for i in range(num1):
        fact*=i+1
    print("Factorial is ", fact)
    