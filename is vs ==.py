# is  -   reference equality - two references refer two the same object
#
# ==  -   value equality  - Two object have the same value
#a=b means a and b refer two same object(memory location)

a=[1,2,3,4]

b=a

b.append(23)

# print(a)

d=[10]

g=d.copy()

print(g is d) # it will print false bcoz g and d point to different object