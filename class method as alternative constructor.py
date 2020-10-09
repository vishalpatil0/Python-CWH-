class Student:
    def __init__(self,name,age,addr):   #__init__(self)==constructor in python 
        super().__init__()
        self.name=name
        self.age=age
        self.addr=addr
    
    @classmethod
    def from_str(cls,string):
        # params=string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split('-'))   #onliner option for above code
    


vishal=Student("Vishal",20,"Kurha")

namu=Student.from_str("namrata-19-Pune")


print(namu.age)
