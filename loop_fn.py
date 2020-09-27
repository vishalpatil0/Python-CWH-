list1=("vishal","patil","namrata","badge")

for item in list1:
    print(item)

full_name=[['vishal','paitl'],['nmarata','badge'],['anjali','munde'],['titiksha','jagtap']]

for name,surname in full_name:
    print(name,surname)

#changing list into dictionary by typecast function  

d1=dict(full_name)
print(d1)

for a in d1.items():
    print(a)

list1=[1,2,3,4,333,44,22,11]

for item in list1:
    if item%2==0 and item>1:
        print(item)
        
for item in list1:
    print(item)
    if item>30:
        break   