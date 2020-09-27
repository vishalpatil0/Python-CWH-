import random

r=random.randint(0,7)

print(r)

bf=random.random() *123

print(bf)


list1=["vishal",'d','pachpande']

print(random.choice(list1))

import platform
x=platform.system()
print(x)

import os

print(os.path.exists("text file1.txt"))



import time

print("this is printed immediately")
time.sleep(2)
print("this is printed after 2 seconds")