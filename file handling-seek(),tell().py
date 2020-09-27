f=open("text file1.txt")
print(f.tell())  #tell() return where is the pointer is 
print(f.readline())
print(f.tell())
f.seek(0) #this place the pointer at given position e.g here with place the pointer at 0
print(f.readline())
print(f.tell())
f.close()