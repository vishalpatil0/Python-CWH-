string_1="hello this string 1"  #this is simple string variable
print(string_1)  #string is printed here
"""
string is the array of characters and as like array it's index start with 0
example :-   
             -5 -4 -3 -2 -1  =index in reverse order            
             h  e  l  l  o   = string (array of characaters) 
             0  1  2  3  4   =index in normal order
""" 
print(string_1[0]) #prints the character at 0 position

print(string_1[0:5])  #this mode prints the character from 0 index to 4th index 

print(len(string_1))  #prints the len of the string

print(string_1[0:])  # we didn't provide the last position here so it automatically take the last of index of the stirng

print(string_1[:5]) #we didn't provide the first index so it automatically take 0 as first index 

print(string_1[0:5:2]) #here the 2 means while print hello ([0:5]) it skips by 1 so output will be hlo
#Note:  we cannot write print(string_1[0:5:0]) like this because ValueError: slice step cannot be zero

print(string_1[:])  #no index is provided here so it takes 0 as first index and string's length as last index

print(string_1[-4:-2])

print(string_1[ : :-1]) #by writing slicing value as -1 we can reverse the string

#function of string as follow

print(string_1.isalnum()) #check if the string is alpha(no spaces) numberic 

print(string_1.endswith("1")) #check if the string ends with giver characters provided in endswith() function

print(string_1.count('o')) #count the number times given character in count() function appeared in the string

print(string_1.capitalize()) #capitalize() function capitalize the first charater of the string

print(string_1.upper()) #convert into upper case

print(string_1.lower()) #convert inot lower case

print(string_1.find('this')) #find the starting index of the provided word in string 

print(string_1.replace('hello','namaste'))


str1=input("Enter the string here")
print("centre allignment;",str1.center(20));
print("centre allignment;",str1.ljust(20));
print("centre allignment;",str1.rjust(20));

name1="vishal";
for x in name1:
	print(x)
print(str1.title()); 
print(str1.swapcase());	 #change the case of every character

print("alphanumeric==",str1.isalnum())
print("digit==",str1.isdigit())
print("alphabet==",str1.isalpha())
print("lower case==",str1.islower())
print("upper case==",str1.isupper())

print(str1.endswith("al"))
print(str1.startswith("vi"))
str1='vishal/gajanan/patil'
print(str1.split('/')) # if there is space in string then the word divided by space get into list as different element

print(str1)
print('+'.join(str1.split()))  #add + every element in string