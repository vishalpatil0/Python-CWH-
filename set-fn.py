#set is collection of well defined and non-repeatative elements No repetition of elements is allowed in sets. 
#easiest way to create set is through list
s=set()
print(type(s))
l=[1,2,3,4]
s1=set(l)
print(s1,"\n type of set s1 (which is created using predefined list) is = ",type(s1))

s1.add(10)  #set only have distinct elements so you can not element which are already present
print(s1)

print(s1.union([1,2,10,19,13])) 
 print(s1.intersection({1,10,13,18})) #prints intersection of 2 sets

 s2=({11,22,33,44})
 s3=({11,22,34,54})
 print(s2.union(s3)) #union of two set s2 and s3

 print(len(s3)) #print lenght of set

 print(max(s3)) #minimum value
 print(min(s3)) #maximum value
 s3.remove(11)  #removes  the value
 print(s3)