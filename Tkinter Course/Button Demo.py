from tkinter import *
from functools import partial   #we imported this to pass argumetns in function when button is pressed
import pyautogui            #we imported pyautogui to pop out alert box when buttons are pressed

def press(strin):
    '''
    This function takes argument as string and create alert box
    '''
    pyautogui.alert(f"You press {strin}")

root=Tk()
root.geometry('655x333')
b1=Button(fg='red',bg='yellow',text="Click",command=partial(press,'Button-1'))
'''
Note: we can't write function as press() infront of command=press() in button
        so we need to write only press not parenthesis and by this we can't pass arguments 
        to solve this problem we imported partial method from functools module
        this method helps to crete a object which don't need parethesis to pass arguments
        e.g     press_with_arg=partial(method_name,parameter) 
'''
b1.pack(anchor='n',side=BOTTOM,fill=X,pady=20)
b2=Button(fg='red',bg='yellow',text="Click",command=partial(press,'Button-2'))
b2.pack(anchor='n',side=BOTTOM,fill=X)
root.mainloop()