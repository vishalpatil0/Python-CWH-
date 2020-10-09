class Student:
    no_of_leaves=9
    def printdetails(self):
        print(f"{self.name}\n{self.age}\n{self.addr}")

    @classmethod
    def change_leaves(abcd,no_of_leaves):  # classmethod are used to chagne the values of class variable
        abcd.no_of_leaves=20



vishal=Student()
namrata=Student()

vishal.name="Vishal Gajanan Patil"
vishal.age=20
vishal.addr="Kurha"
namrata.name="Namrata Laxman Badge"
namrata.age=19
namrata.addr="Pune"

vishal.printdetails()
namrata.printdetails()

print("vishal no of leaves= ",vishal.no_of_leaves)
print("namrata no of leaves= ",namrata.no_of_leaves)

Student.change_leaves(38)

print("after using class method changeleaves")

print("vishal no of leaves= ",vishal.no_of_leaves)
print("namrata no of leaves= ",namrata.no_of_leaves)
