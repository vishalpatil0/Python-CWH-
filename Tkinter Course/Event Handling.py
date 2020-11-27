from tkinter import *

def show(event):
    print(f"hello ji{event.x} {event.y}")

root=Tk()
root.title("Event Handling")
root.geometry("700x400")

widget=Button(text="click me")
widget.pack()

widget.bind('<Button-1>',show) #bind function bind the button with certain event
widget.bind('<Double-1>',quit)
#like this we can bind differnt types of event to this

if __name__ == '__main__':
    root.mainloop()
