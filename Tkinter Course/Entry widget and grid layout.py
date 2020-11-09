from tkinter import *
import pyautogui

root=Tk()
def reset():
    uservalue.set('')
    passvalue.set('')
root.geometry('655x333')
def submit():
    pyautogui.alert("Values successfully submitted.")

user=Label(root,text='UserName')
password=Label(text='Password')
user.grid()
password.grid(row=1)
'''
variable classses in tkinter
BooleanVar,DoubleVar,IntVar,StringVar
'''

uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text='Reset',command=reset).grid()
Button(text='Submit',command=submit).grid(row=2,column=1)

root.mainloop()