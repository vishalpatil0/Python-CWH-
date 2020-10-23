# def funct(args):
#     for i in args:
#         print(i)


# jp=("ram","shyam","mohan","john","ron", "son")
# funct(jp)



def listaccept(gh):
    print(type(gh))
    for i in gh.items():
        print(i)


vish={1:10,2:20,3:30,4:40}
listaccept(vish)

# def adder(*args):  
#     """args  we can pass number of arguments to args and it convert everthing in tuple  """
#     print("type of args is = ", type(args))
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)

# adder(2,2,3,4)    
# print(adder.__doc__)

# #kwargs   


def accet3(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for i in kwargs.items():
        print(i)

accet3(firstname="vishal",secondname="patil")

def accept4(asd):
    print(type(asd))
    for i in asd.items():
        print(i)

dict3={"vishal":"patil","namrata":"badge"}
accept4(dict3)        