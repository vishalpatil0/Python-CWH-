from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()

root.geometry("700x400")
root.title("RadioButtons")

def letsgo():
    tmsg.showinfo("Your Order",f"We have received your order for {var.get()}.")

var=StringVar()     #string class
var.set("Nothing")    #setting default one
Label(root,text="What would you like to have sir?",pady=15,font="lucida 19 bold",justify=LEFT).pack()

radio=Radiobutton(root,text="Dosa",variable=var,value="Dosa").pack(anchor='w',padx=150)
radio=Radiobutton(root,text="Idli",variable=var,value="Idli").pack(anchor='w',padx=150)
radio=Radiobutton(root,text="Uttappa",variable=var,value="Uttappa").pack(anchor='w',padx=150)
radio=Radiobutton(root,text="Pohe",variable=var,value="Pohe").pack(anchor='w',padx=150)

Button(text="Submit",command=letsgo).pack()
root.mainloop()
