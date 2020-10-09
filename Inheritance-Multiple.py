class Student:
    def __init__(self,name,age,addr):   #__init__(self)==constructor in python 
        self.name=name
        self.age=age
        self.addr=addr
    
    def printdetails(self):
        print(f"{self.name}\n{self.age}\n{self.addr}")

class player:
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def print1(self):
        print(f"{self.name}\n{self.game}")

class coolprogrammer(Student,player):
    lang="C++"

    def print2(self):
        print("Language=",self.lang)


vishal=coolprogrammer("vishal",20,"pune")
vishal.game="kho kho"
vishal.print1()