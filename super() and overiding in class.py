# Note  object first look for instance variable after that they look for class variable

#note if we override something then the first defined thing don't get executed even if the statments in second things are comment outed

class A:
    classvar1="I am class A variable"

    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="Instance var of class A"
        self.special="special"

class B(A):
    classvar1="I am in class B"
    def __init__(self):
        super().__init__()
        self.var1="i am inside class b's constructor"
        self.classvar1="Instance var in class b"
        print(super().classvar1)
a=A()
b=B()

print(b.special,b.var1,b.classvar1)
