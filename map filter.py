list1=('1','2','3','4','5')
try:
    sum1=0
    for i in range(len(list1)):
      sum1+=list1[i]


    print(sum1)

except Exception as e:
    print(e) 

def sqi(b):
    return b*b

 
a=list(map(int,list1))   #map function apply the function of every element of list
sum1=0
for i in range(len(a)):
    sum1+=a[i]

#NOTE  MAP FUNCTION ONLY REUTRN OBJECT 
print(sum1)   

j=list(map(sqi,a))

print(j)


def sq(a):
    return a*a

def cube(a):
    return a*a*a

def adder(a):
    return a+a



func=[sq,cube]

for i in range(1,5):
    list3=list(map(lambda x: x(i),func))
    print(list3)


##############filter#########################

#difference between map and filter function is that map gives the ouptut of the function 

# and filter giver the value of the list which is passed if the output of the applies function is true

list1=[1,2,3,4,4]

def is_greater_than_2(a):
    return a>2

a=list(filter(is_greater_than_2,list1))
print(a)

# as input to filter function is only true or false


#########################Reduce##############################

#Reduce function return the value like int,float,str but map function only return object which is only can be converted in list or tuple
from functools import reduce
print(reduce(lambda x,y:x+y,list1))
