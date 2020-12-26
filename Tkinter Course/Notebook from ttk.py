#import tkinter and ttk modules
import tkinter
from tkinter import ttk

#Make the root widget
root = tkinter.Tk()
root.geometry('600x300')
#Make the notebook
nb = ttk.Notebook(root)
nb.grid()

#Make 1st tab
f1 = tkinter.Frame(nb)
ttk.Label(f1,text='vishu').place(x=70,y=40)
#Add the tab
nb.add(f1, text="First tab")

#Make 2nd tab
f2 = tkinter.Frame(nb)
ttk.Label(f2,text="namu").place(x=30,y=30)
#Add 2nd tab 
nb.add(f2, text="Second tab")

nb.select(f2)

nb.enable_traversal()

#Enter the mainloop
root.mainloop()