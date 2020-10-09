import numpy as np

list1=[1,2,3,4,5]

a=np.array(list1)

print("a.size =", a.size)
print("a.ndim =", a.ndim) #print the total number of dimension of array
print(type(a))
print(a.dtype)

a=np.array([1,0])
b=np.array([0,1])
c=a+b
print(c)
d=c*2
print(d)
print("mean =",a.mean())
print("max =",a.max())

a=[[1,2,3],[4,5,6],[7,8,9]]

a=np.array(a)
print(a)
print(a[1,0:2])