import datetime

def gettime():

    return datetime.datetime.now()

dict1={"1":"Harry","2":"Rohan","3":"Hammad"}

def take(k):

    if k==1:

        c=int(input("enter 1 for excersise and 2 for food"))

        if(c==1):

            value=input("type here\n")

            with open("harry-ex.txt","a") as op:

                op.write(str([str(gettime())])+": "+value+"\n")

            print("successfully written")

        elif(c==2):

            value = input("type here\n")

            with open("harry-food.txt", "a") as op:

                op.write(str([str(gettime())]) + ": " + value + "\n")

            print("successfully written")

    elif(k==2):

        c = int(input("enter 1 for excersise and 2 for food"))

        if (c == 1):

            value = input("type here\n")

            with open("rohan-ex.txt", "a") as op:

                op.write(str([str(gettime())]) + ": " + value + "\n")

            print("successfully written")

        elif (c == 2):

            value = input("type here\n")

            with open("rohan-food.txt", "a") as op:

                op.write(str([str(gettime())]) + ": " + value + "\n")

            print("successfully written")

    elif(k==3):

        c = int(input("enter 1 for excersise and 2 for food"))

        if (c == 1):

            value = input("type here\n")

            with open("hammad-ex.txt", "a") as op:

                op.write(str([str(gettime())]) + ": " + value + "\n")

            print("successfully written")

        elif (c == 2):

            value = input("type here\n")

            with open("hammad-food.txt", "a") as op:

                op.write(str([str(gettime())]) + ": " + value + "\n")

            print("successfully written")

    else:

        print("plz enter valid input (1(harry),2(rohan),3(hammad)")

def retrieve(k):

    if k==1:

        c=int(input("enter 1 for excersise and 2 for food"))

        if(c==1):

            with open("harry-ex.txt") as op:

                for i in op:

                    print(i,end="")

        elif(c==2):

            with open("harry-food.txt") as op:

                for i in op:

                    print(i, end="")

    elif(k==2):

        c = int(input("enter 1 for excersise and 2 for food"))

        if (c == 1):

            with open("rohan-ex.txt") as op:

                for i in op:

                    print(i, end="")

        elif (c == 2):

            with open("rohan-food.txt") as op:

                for i in op:

                    print(i, end="")

    elif(k==3):

        c = int(input("enter 1 for excersise and 2 for food"))

        if (c == 1):

            with open("hammad-ex.txt") as op:

                for i in op:

                    print(i, end="")

        elif (c == 2):

            with open("hammad-food.txt") as op:

                for i in op:

                    print(i, end="")

    else:

        print("plz enter valid input (harry,rohan,hammad)")

while(True):
    try:
        print("health management system: ")

        Print("\n1-show the current users\n2-add more user")

        a=int(input("press 1 for lock the value and 2 for retrieve "))



        if a==1:
            for key, value in dict1.items():
                print("press",key,"for",value)

            b = int(input())

            take(b)

        else:

            for key, value in dict1.items():
                print("press",key,"for",value)

            b = int(input())
            retrieve(b)
        ip1=int(input("Press 1 to continue = "))
        if(ip1!=1):
            break
    except FileNotFoundError as e:
        print("\n\nPlease enter the details before retrieving it\n")
    except Exception as e:
        print("\n",e,"\n")


