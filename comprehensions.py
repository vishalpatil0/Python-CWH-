list1=[i for i in range(100) if i%3==0]
print(list1)

dict1={i:f"item{i}" for i in range(10)}
dict1={value:key for key,value in dict1.items()}
print(dict1)

set1={st1 for st1 in ['dress1','dress2','dress1','dress2','dress1','dress2','dress1','dress2']}

print(set1)

#generator comprehension

evens=(i for i in range(100) if i%2==0)

print(evens.__next__())
print(evens.__next__())

list1=[]

a=int(input("Enter the limit of the list = "))

for i in range(a):
    d=input(f"enter the {i+1} element = ")
    list1.append(d)
a=int(input("1-List\n2-Set\n3-Dictionary"))

if(a==1):
    list2=[i for i in list1]
    print(type(list2))
    print(list2)
elif (a==2):
    set1={i for i in list1}
    print(type(set1))
    print(set1)
elif(a==3):
    dict1={i:f"item{i}" for i in list1}
    print(type(dict1))
    print(dict1)


