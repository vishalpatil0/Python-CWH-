#recusrion 
#5=5!=5*4*3*2*1

def rec(n):
    if (n==1) and (n==0):
        return 1
    else:
        return (n*rec(n-1))

n=int(input("enter number="))
print("recursion of number is =",rec(n))


# fac=1
# for i in range(n):
#     fac=fac*(i+1)
# return fac
        