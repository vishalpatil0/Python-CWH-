class Student:
    def __init__(self,name,lname):
        self.name=name;
        self.lname=lname;
        # self.email=f"{name}.{lname}@gmail.com"
    
    def printdetails(self):
        print(f"This is {self.name} {self.lname} and her email is = {self.email}")

    @property
    def email(self):
        if self.name==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.name}.{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
        names=string.split("@")[0]
        self.name=names.split(".")[0]
        self.lname=names.split(".")[1]
    @email.deleter
    def email(self):
        self.name=None
        self.lname=None


namu=Student("Namrata","Badge")

namu.lname="Patil"
print(namu.lname)
namu.printdetails()

print(namu.email)

namu.email="this.that@gmail.com"

print(namu.email)

vishal=Student("vishal","patil")
print(vishal.email)
vishal.email="ok.that@gmail.com"
print(vishal.name)

del namu.email

print(namu.email)
print(namu.name)