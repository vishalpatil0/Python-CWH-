

print("How Many Row You Want To Print")

one= int(input())

print("Type 1 Or 0")

two = bool(input())

if two == True:

    for i in range(1,one+1):

        for j in range(1,i+1):

            print("*",end=" ")

        print()

elif two ==False:

    for i in range(one,0,-1):

        for j in range(1,i+1):

            print("*", end="")

        print() 