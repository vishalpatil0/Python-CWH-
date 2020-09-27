#simple way to read file

f=open("text file1.txt")   # f is here a pointer by deafult it at the starting of the file but if we run the same function (for example read() fn) it will give different ouput
print(f.read())
print("Number of characters in this file are==",f.tell())
f.close()

#handling file with mode

f=open("text file1.txt","rb")      #here we open the file in read which is default and binary mode  Note: can't have binary and text mode at once
gh=f.read()
print(gh)
f.close()

f=open("text file1.txt","rt")  #open the file in read and text mode
print(f.read(3))  #3 in the read() function only print first 3 character of string (means data) if the provided value is greater than the lenght of string then it will print whole file


#read() function doesn't work if you had read the whole file so there is another trick
#here in this following loop we read the file line by line and Note: in our text file1.txt we have three line means there are by default 2 "\n" 

for a in f:
    print(a,end="")


#Note readline() function prints only the first line and if we execute the readline() function again it will not only print the first line but also 2nd line and it goes on 

print(f.readline())  #this statement print only the first line  .when  the pointer "f" encounters the new line character "\n" it stop reading the file
print(f.readline())   # this statement does this same it only prints the second line not first line again bcoz pointer start from second line bcoz first same statement


# Note  readlines() function print all the file as a list

print(f.readlines()) # as you can see it prints complete file as a list with "\n" except for last line 