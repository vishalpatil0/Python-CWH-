from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("700x400")
root.title("Sliders")
# myslider=Scale(root,from_=0,to=155)     #vertical slider
# myslider.pack()
# myslider1=Scale(root,from_=20,to=100,orient=HORIZONTAL)     #horizontal slider
# myslider1.pack()

def showthis():
    tmsg.showinfo("Your review.",f"You have rated us with {myslider1.get()} points")

Label(text="Rete this website.").pack()
myslider1=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider1.set(30)
myslider1.pack()
Button(root,text="Click Me",command=showthis).pack()
root.mainloop()