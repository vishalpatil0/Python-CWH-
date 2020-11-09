#Canvas means you can crate line,rectangle,oval and add text on screen with the help of co-ordinate.
from tkinter import *

root=Tk()

canvas_width=800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")
root.maxsize(canvas_width,canvas_height)

cnvs=Canvas(root,width=canvas_width,height=canvas_height)
cnvs.pack()

cnvs.create_line(0,0,800,400,fill='red')
cnvs.create_line(0,400,800,0,fill='red')

cnvs.create_rectangle(100,50,600,300) 

cnvs.create_text(200,200,text="Python",fill='green')

cnvs.create_window(400,400)

root.mainloop()