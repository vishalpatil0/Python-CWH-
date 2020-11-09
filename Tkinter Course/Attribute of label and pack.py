from tkinter import *

root=Tk()

root.geometry("1000x600")

"""Important label options
text=add the text
bg=background  you can use bg or background
fg=foreground
font=sets the font
padx=x padding
pady=y padding
relief=border styling -SUNKEN, RAISED, GROOVE, RIDGE"""

text_label=Label(text='''Hellot this is vishal patil.\nAnd this is my home where is live.\nWhat is the cost of lies?''',    
                bg='red',
                fg='blue',
                pady=33,
                padx=30,
                font=("comicsansms",19,'bold'),  #font="comicsansms 19 bold"
                borderwidth=5,
                relief=SUNKEN
                )
'''
IMPORTANT PACK OPTIONS
anchor=nw nw=north west and ne=north east & anchor sets the location
side=top,bottom,left,right
fill=
padx
pady
'''
# text_label.pack(side='bottom',anchor='sw',fill=X)
text_label.pack(padx=20,pady=200)
root.mainloop()