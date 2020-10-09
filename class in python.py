#class is nothing but a template to store data
#object is the instance of the class by using object we can acces the elemnt of the class
class student:
    no_of_leaves=9
    pass #pass means nothing 

vishal=student()  #this is the way to create object in python 
namrata=student()

print(f"memory location of object =  {vishal}\n memory location of object =  {namrata}")

vishal.name='Vishal Gajanan Patil'
vishal.age=20
vishal.addr='Kurha'

namrata.name="Namrata Laxman Badge"
namrata.age=20
namrata.addr="pune"

list1=[vishal,namrata]
vishal.no_of_leaves=10
for i in list1:
   print(i.name)
   print(i.age)
   print(i.addr)
   print(i.no_of_leaves)

print(vishal.__dict__)  #__dict__ this function helps to see all the atributes which are presents in  object
print(namrata.__dict__)  #__dict__ this function helps to see all the atributes which are presents in  object
