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


vishu=Student("vishal","patil")

print(id(vishu))

print(id("nobody is perfect"))   #it gives the id of the object Every object have a special unique ID

print(dir(vishu)) #dir fn gives all the applicable method of object
print(vishu.__class__)

import inspect

print(inspect.getmembers(vishu))