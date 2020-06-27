#----- Import Library -----#
from tkinter import font
from tkinter import messagebox
import tkinter as tk # For root
import tkinter.ttk as ttk # More modern library
import time
from PIL import ImageTk, Image

root = tk.Tk()
delay=tk.Entry(root)

def ya():
    global buat
    buat = ttk.Button(root, text = "Buat", command= lambda: ga())
    buat.grid(column=0, row=0)
    
    global huhu
    huhu = ttk.Button(root, text = "Batal")    
    
def ga():
    idelay = delay.after(3000,ga())
    def callback(event):
        if True:
            print("clicked2")
            # 'solve' is used here to stop the after... methods.
            delay.after_cancel(idelay())

    huhu.bind("<Button-1>",callback)
    huhu.grid(column=0, row=1)
    
    global apus
    apus = ttk.Button(root, text = "Apus")
    apus.grid(column=0, row=1)
    
ya()
    
root.mainloop()