from tkinter import *

def myfunc():
    print("hello this is ok")
root=Tk()

root.geometry("700x400")
root.title("Menus and Submenus")

#use this to create a non-drop down menu
# myMenu=Menu()
# myMenu.add_command(label="File",command=myfunc)
# myMenu.add_command(label="Exit",command=quit)
# root.config(menu=myMenu)


#submenus
myMenu=Menu(root)

m1=Menu(myMenu,tearoff=0) #tearoff=0 means the submenu can't be teared of from the window
m1.add_command(label='new',command=myfunc)
m1.add_command(label='print',command=myfunc)
m1.add_separator()# this add a line between submenus
m1.add_command(label='open',command=myfunc)
m1.add_command(label='help',command=myfunc)
root.config(menu=myMenu)

myMenu.add_cascade(label="File",menu=m1)
root.mainloop()