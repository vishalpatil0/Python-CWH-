#note  'r+'  === is read write mode

f=open("text file2.txt","r+")


print(f.read())

f.write("thank you")

f.close()