from tkinter import *

root=Tk()
root.title("Text Editior")
root.geometry('800x500') 
f1=Frame(root,bg='red',borderwidth=6,relief=RAISED)
f1.pack(side=LEFT,fill='y')
l=Label(f1,text="Projects",fg='blue',pady=200)
l.pack(pady=142)
f2=Frame(root,bg='green',borderwidth=5,relief=SUNKEN)
f2.pack(side=TOP,fill='x')
l2=Label(f2,text="Welcome to the projects.",fg='grey')
l2.pack()
root.mainloop()