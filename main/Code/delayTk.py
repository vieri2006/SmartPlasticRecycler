from tkinter import *

def blink():
    e.after(1000, lambda: aa())

root=Tk()
e=Entry(root)
b=Button(root, text='blink', command= lambda: blink())
b.pack()

def aa():
    i=Entry(root, bg='white')
    i.pack()


root.mainloop