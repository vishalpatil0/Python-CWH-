l1=[1,2,3,4,5]

print("list")

for index,item in  enumerate(l1):
    print(index)


l2=(1,2,3,4,5)
print("tuple")
for index,item in  enumerate(l2):
    print(index)

print("dictionary")
dict1={1:10,2:20,3:30}

for index,item in  enumerate(dict1):
    print(f"{index} = {item}")


