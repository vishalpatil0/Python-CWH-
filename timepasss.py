import datetime
def gettime():
    return datetime.datetime.now()

def write1(a):
    with open("student-data1.txt",'a') as f:
        f.write(str([str(gettime())])+":"+a+"\n")

def read1():
    with open("student-data1.txt") as f:
        for u in f:
            print(u,end="")

while(-4):    
    ip1=int(input("Press 1 to enter the data\nPress 2 to read the data\n="))

    if (ip1==1):
        a=input(("Enter the name of student = "))
        write1(a)
        ip2=int(input("if you want to continue press 1"))
        if(ip2!=1):
            break
    
    elif(ip1==2):
        read1()
        ip2=int(input("if you want to continue press 1"))
        if(ip2!=1):
            break
    else:
        print("please enter vaild choice\n")


# print(open("text file1.txt"))