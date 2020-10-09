import datetime
import os
def gettime():
    return datetime.datetime.now()

def write1(a):
    if(os.path.exists("student-data1.txt")):
        with open("student-data1.txt",'a') as f:
            f.write(str([str(gettime())])+":"+a+"\n")
    else:
        with open("student-data1.txt",'w') as f:
            f.write(str([str(gettime())])+":"+a+"\n")

def read1():
    if(os.path.exists("student-data1.txt")):
        with open("student-data1.txt") as f:
            for u in f:
                print(u,end="")
    else:
        print("file not present so please enter the data first")

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