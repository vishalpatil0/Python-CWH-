from tkinter import *           #importing all classes and methods from tkinter package


root=Tk()                       #creating instance of TK() class it aslo creates basic gui 

#gui logic here
root.geometry("700x500")        #width X height

root.minsize(200,80)            #can't minimize it more than this size
root.maxsize(1000,800)          #can't maximize it more than this size

if __name__=="__main__":
    root.mainloop()             #mainloop() function launche the basic gui created by (crating the instance of Tk class)
