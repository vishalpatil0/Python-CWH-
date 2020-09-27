list1=["vishal","gajanan","patil",34]

print(list1)
print(list1[2])
print(list1[ : :2])

list2=[14,28,13,4] 
list2.sort() #sort 
list2.reverse() #reverse the code
print(list2)

print(len(list2)) #length of string

list2.append(334) #add 334 at the end of the stirng if we provide list here like [33,22] instead of single elements it enter the entire provided list in the list as nested list

list2.insert(2,980) #insert 980 at the 2 index

list2.remove(13) #remove 13 fromt the list
print(list2)
list2.pop() #removes the last element of list
print(list2)
"""
Mutable = can change
Immutable =can not change

touple are immutable and list are mutable 

e.g of list
a=[1,2,3]

e.g of touple
a=(1,3,4)

tp=(1) output of this touple is 1 bcoz interpreter think tp as a integer and we put bracket just of safety so it is necessary to put (,) in touple as tp=(1,)
"""
tp=(1,2,3)
print(tp)
print(type(tp)) 
print(type(list1)) 
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 
del tuple1
del tuple2
print("touple3.count(2)==",tuple3.count(2))
print("tuple3.index(2)==",tuple3.index(2))
print(tuple3[1])
"""
temp=a
a=b
b=temp
this is traditional way to swap two numbers
but in python

a,b=b,a   is this simple
"""

a=[1,2,3,[3,4]]

print(a[3][1])
b=[222,33,444]
a.extend(b) #extend teh list with another list 
print(a)

vishal=[1,2,[3,4,[5,6]]] #example of matrix i.e. three dimensional array

print(vishal[2][2][1])

print(vishal.index([3,4,[5,6]]))

patil=[1,2,3,4,5,6,7,8,9]
print(patil.index(7,2,7))

list3=[1,2,3,4]
tupled=tuple(list3)

print(tupled)