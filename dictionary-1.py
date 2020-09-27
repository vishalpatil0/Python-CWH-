#program to take create dictionary and take input (keys) from user and give the result which is value

d1={"vishal":"patil","namrata":"badge","mayur":"dhakane"}

search=input("please give the keys = ")

if(d1.get(search)==None):
    print("go to hell")
else:
    print(d1[search])


