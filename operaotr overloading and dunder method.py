class Student:
    def __init__(self,name,age,addr):   #__init__(self)==constructor in python 
        self.name=name
        self.age=age
        self.addr=addr
    
    def printdetails(self):
        print(f"{self.name}\n{self.age}\n{self.addr}\n{self.year}")

    def __add__(self, other):   #  dunder method override print function to add age of 2 objects
        return (self.age+other.age) #search mapping operator to functions on google for more opertor overloading    
    def __truediv__(self,other):
        return (self.age/other.age)
    def __repr__(self):
        return(f"Student({self.name},{self.age},{self.addr})")
vishal=Student("Vishal",20,"Kurha")
namu=Student("namrata",20,"pune")

print(vishal+namu)
print(vishal)