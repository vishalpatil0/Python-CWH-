
def fib(n):
    first=0
    second=1
    next1=0
    for i in range(0,n):
        if(i<=1):
            next1=i
        else:
            next1=first+second

            first=second
            second=next1
        print(next1)

ip1=int(input("enter the input here"))
fib(ip1)