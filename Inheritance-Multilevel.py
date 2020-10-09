class grandfather:
    _sing=1
    __football=10  #python saves private variable as _classname__variablename to protect if you ever use it outside accidentlly

class father(grandfather):
    dance=1
    def isdance(self):
        print(f"is can dance {self.dance} no of times")

class son(father):
    dance=10
    def isdance(self):
        print(f"i can dance {self.dance} times")
    

gulabrao=grandfather()
gajanan=father()
vishal=son()

vishal.isdance()

print(gulabrao._sing)
print(gajanan._sing)
print(vishal._sing)

print(gulabrao._grandfather__football)
