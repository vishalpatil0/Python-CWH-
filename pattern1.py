
print("*\n**\n***\n****\nDo you want to print this pattern\nIf yes then enter 1 else 0")
a=int(input())
b=bool(a)
print("enter number of lines you want to print this pattern")
n=int(input())
if(b==True):
    i=0
    while(i<n):
        j=0
        while(j<i+1):
            print("*",end="")
            j+=1  
        print()
        i+=1
else:
    i=n
    while(i>0):
        j=i
        while(j>0):
            print("*",end="")
            j-=1
        print()
        i-=1