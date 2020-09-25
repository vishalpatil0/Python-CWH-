#this is program of basic variable, concatenation and type casting

var1="hello world"
var2="vishal"
var3=334
var4=3.44

print(var3+var4) #output  334+3.44=337.44

var5=var1+" "+var2  #concatenation of two strings

print(var5)

print("type of var1 varibale is = ",type(var1))

var6=type(var4)

print("type of var4 variable is = ",var6)

var7=int(var4)
print("After typecasting var4=",var4," which is float into integer == ",var7)

print(end="")
print("\t ",float(var3))