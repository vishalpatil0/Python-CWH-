#dictionary is nothng but key value pair
#square bracket [] are for list 
#() parenthesis are for touple which are immutable
#{} curli bracket are for dictionary

#NOTE: VALUE OF DICTIONARY CAN LIST, TOUPLE AND DICTIONARY and key are immutable like constants e.g. string,integer,float 

d1={}

print(type(d1))

d2={"vishal":"patil","namrata":"badge","divya":{"a":"apple","b":"bananan","c":{"ab":"aaba","tmt":"tommato"}}} #dictionary within a dictionary withia a dicionary

print(d2["divya"]) #put the dictionary of divya
print(d2["divya"]["c"]["tmt"]) #put the dictionary of divya and the value of c
# print(d2[2]) this is not allowed in dictionary bcoz we it only take keys in this form 
d2={"anjali":"munde"} #we alreay created the dictionary with d2 name so this statement reinitialize the dictiory form scratch
d2["shweta"]="phengale" #adding entry in already created dictionary k
del d2["shweta"] #delete the entry in the dictionary
print(d2)


d2={"vishal":"patil","namrata":"badge","divya":{"a":"apple","b":"bananan","c":"carrot"}} #dictionary within a dictionary
print("ithun bagh")
print(list(sorted(d2.keys())))  # list convert dictionary into list and sorted fn() sort it out


d3=d2 # by doing this if do any operation like adding or deleting entry in d3 it also affect d2 because they both address to same memory location 

d4=d2.copy() #by this statement it create the copy of d2 in d4 and operation of d4 doesn't affect d2 bcoz d4 have its own copy and they addres to different memory location 

print(d3.get("vishal")) #print the value of key 

d4.update({"shruti":"amle"}) #add the new entry at the end of existing dictionary

print(d4)

print(d4.keys()) #print the keys of dictionary
print(d4.values()) #print the values of dictionary
print(d4.items()) #print the all key value pairs

dict4=dict.fromkeys(d2)  #it only gives keys of d2 dictionary to dict4 and values as none
print(dict4)

print(d2.setdefault("vishal"))
print(d2)

d2.popitem() #pop out the last item
d2.pop("vishal") #pop out the specific key with values 
print(d2)

d2.clear() #empty the dictionary
print(d2)
del d2

#dictionary comprehension

square={x:x*x for x in range(6)}
odd_square={x:x*x for x in range(6) if x%2!=0}

print(square)



print(odd_square)
