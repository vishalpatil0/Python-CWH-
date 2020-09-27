#binary search in python
limit1=int(input("enter the limit of array = "))
i=0
list1=[]
while(i<limit1):
    print("enter the ",i+1,"th element")
    list1.append(int(input()))
    i+=1

print("User provided list is = ",list1)

search=int(input("enter the element to serach = "))
f=0
low=0
high=limit1-1
mid=int((low+high)/2)

for i in range(0,limit1):
    if search==list1[mid]:
        print(search," found at ",mid+1,"th position")
        f=1
        break
    elif search>list1[mid]:
        low=mid
        mid=int((low+high)/2)
    elif search<list1[mid]:
        high=mid
        mid=int((low+high)/2)

if(f==0):
    print("not in the list")
