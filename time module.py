import time

initial=time.time()
print(initial)

i=0
while(i<50):
    print(end="")
    i+=1
print(time.time())
a=time.time()-initial
print(f"time taken by while loop to execute = {a}")

for i in range(0,50):
    print(end="")

initial1=time.time()
print(initial1)
print(f"time taken by for loop to execute = {time.time()-initial}")