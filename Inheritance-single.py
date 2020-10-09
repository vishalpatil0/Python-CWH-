class Student:
    def __init__(self,name,age,addr):   #__init__(self)==constructor in python 
        self.name=name
        self.age=age
        self.addr=addr
    
    def printdetails(self):
        print(f"{self.name}\n{self.age}\n{self.addr}")

class Programmer(Student):
    def __init__(self,name,age,addr,lang):
        self.name=name
        self.age=age
        self.addr=addr
        self.languages=lang

vishal=Student("Vishal",20,"Kurha")
kanya=Programmer("namu",20,"pune",['c','c++',"python"])

kanya.printdetails()