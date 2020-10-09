f1=open("file basics.txt")

try:
    f2=open("text file1.txt")
except FileNotFoundError as e:
    print(e)
else:
    print("this will print if except not get executed")
finally:
    print("this is finally")
    f1.close()