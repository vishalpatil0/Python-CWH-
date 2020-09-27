with open("text file1.txt") as f:
    print(f.read(3))


#Note:  with block automatically closes the file so there is need to write the close() function

# f=open("text file1.txt")
# print(f.read())