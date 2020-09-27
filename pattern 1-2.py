try:
    ip1=int(input("enter the nubmer of rows"))

    for i in range(0,ip1+1):
        print(i*"*")

    for i in range(ip1,0,-1):
        print(i*"*")

except Exception as e:
    print("Invalid input = ",e)