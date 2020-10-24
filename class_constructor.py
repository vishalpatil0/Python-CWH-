class Student:
    def __init__(self,name,age,addr):   #__init__(self)==constructor in python 
        super().__init__()
        self.name=name
        self.age=age
        self.addr=addr
    
    def printdetails(self):
        print(f"{self.name}\n{self.age}\n{self.addr}\n{self.year}")


vishal=Student("Vishal",20,"Kurha")

vishal.year=2000
print(vishal.year)

