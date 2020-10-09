from abc import ABC,abstractclassmethod

class shape(ABC):
    @abstractclassmethod    
    def printarea(self):
        return 0
    
class rectangle(shape):
    def __init__(self):
        self.length=10
        self.bridth=20
    
    def printarea(self):
        return self.length*self.bridth

b=rectangle()

print(b.printarea())