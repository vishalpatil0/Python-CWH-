#string formatting
a="vishal is  poor boy"

b="so vishal is what?%s"%a

print(b)

d=3

e="vishal"

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