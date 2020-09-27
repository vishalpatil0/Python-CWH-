#string formatting
a="vishal is a poor boy"

b="so vishal is what?%s"%a

print(b)
d,e=('vishal',3)

c="so %s and %s"%(d,e)
print(c)


a="this is {} {}"
b="vishal"
c=3

print(a.format(b,c))

#all this method we saw are old ways

#there is a  new ways

a=f"this is {b} {c} {4*34}"  #f indicate that it is a fstring
print(a)