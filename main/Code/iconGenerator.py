#----- Import Library -----#
from tkinter import font
import tkinter as tk # For root
import tkinter.ttk as ttk # More modern library
import time
from PIL import ImageTk, Image

root = tk.Tk()

logo_ori = Image.open("Kosong.png")#buat logo sesuai keperluan ukuran
logo60 = logo_ori.resize((60, 740), Image.ANTIALIAS)
logo60.save("pinggir.png")

logo60 = tk.PhotoImage(file="pinggir.png") #import ke py
logo = ttk.Label(root, image=logo60, background='white')
logo.grid(column=0,row=0)

root.mainloop()
