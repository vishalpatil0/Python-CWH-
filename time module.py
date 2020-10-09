import time

initial=time.time()
print(initial)

i=0
while(i<50):
    print(end="")
    i+=1

print(f"time taken by while loop to execute = {time.time()-initial}")

for i in range(0,50):
    print(end="")

initial=time.time()

print(f"time taken by for loo loop to execute = {time.time()-initial}")