#Arithemtic operators
print("50+2 = ",50+2)
print("50-2 = ",50-2)
print("50*2 = ",50*2)
print("50/13 = ",50/13)  # answer is 3.8461538461538463
print("50%2 = ",50%2)
print("50//13 = ",50//13) # answer is 3 not 3.8461538461538463 bcoz // opearator gives answer only in integer
print("50**2 = ",50**2)  # 50^2 = 50*50 

#Assignment opeartors

x=12 
x+=12 

#Comparision operators

print(2==1)  #gives the comparision value i.e. true or false
print(3>2)
print(3!=4)

#Logical opearator

a=True
b=False

print(a and b)
print(a & b)   #for and all must be true to run the condition
print(a or b)    #for or all even if only one condition is true the it run the statement
print( a | b)
#Identical operator

a=3
b=4
print(a is not  b)
print(a is b)

#Membership operatorss

list1=[1,2,3,4,5,6]
print(3 in list1)
print(2 not in list1)

#Bitwise opearator
#0 00
#1 01
#2 10
#3 11
# like wise binary

print(1 & 0)  # anding happened here means mulitiplication of 00 and 01 which is obiviously 00 so the output is 0 here
print( 2 & 2)

print(10 | 4)

print(~10)

print(10 ^ 4)

print(15>>2)   #15=1111 right shift the right bit and fill the void space at left with 0  here we shift by 2 bit in right
print(15<<2)

     
