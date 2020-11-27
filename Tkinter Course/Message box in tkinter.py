from tkinter import *
import tkinter.messagebox as tmsg

def ok():
    a=tmsg.showinfo("Help","Vishal will help you")
def rateus():
    a=tmsg.askquestion("is this okay")
    tmsg.showinfo("k",a)
root=Tk()

root.geometry('700x400')
root.title("Message box")

MainMenu=Menu(root)

m1=Menu(MainMenu,tearoff=0)
m1.add_command(label="New",command=ok)
m1.add_command(label="Open",command=ok)
m1.add_command(label="Save",command=ok)
m1.add_command(label="Save as",command=ok)
MainMenu.add_cascade(label="File",menu=m1)
root.config(menu=MainMenu)

m2=Menu(MainMenu,tearoff=0)
m2.add_command(label="Cut",command=ok)
m2.add_command(label="Paste",command=ok)
m2.add_command(label="Copy",command=ok)
MainMenu.add_cascade(label="Edit",menu=m2)
root.config(menu=MainMenu)

m3=Menu(MainMenu,tearoff=0)
m3.add_command(label="Help",command=ok)
m3.add_command(label="Rate us",command=rateus)
MainMenu.add_cascade(label="Help",menu=m3)
root.config(menu=MainMenu)
root.mainloop()