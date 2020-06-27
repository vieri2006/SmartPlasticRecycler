import tkinter as tk
import tkinter.ttk as ttk

class App(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.geometry('900x200')
		self.title('Page test')

		self.frame1 = ttk.Frame(self)
		self.frame1.grid(sticky = 'nsew')

		self.next_btn = ttk.Button(self.frame1,text = 'Next',command = self.frame2_visible)
		self.next_btn.grid(sticky = 'se')

		self.frame2 = ttk.Frame(self)

		self.back_btn = ttk.Button(self.frame2,text = 'Back',command = self.frame1_visible)
		self.back_btn.grid(column = 2,sticky = 'sw')

	def frame2_visible(self):
		self.frame1.grid_remove()
		self.frame2.grid(sticky = 'nsew')

	def frame1_visible(self):
		self.frame2.grid_remove()
		self.frame1.grid(sticky = 'nsew')

App().mainloop()

''' Styling in ttk	
from Tkinter import *
import ttk

p = Tk()

p.geometry('600x350')
p.configure(bg='#334353')

gui_style = ttk.Style()
gui_style.configure('My.TButton', foreground='#334353')
gui_style.configure('My.TFrame', background='#334353')

frame = ttk.Frame(p, style='My.TFrame')
frame.grid(column=1, row=1)

ttk.Button(frame, text='test', style='My.TButton').grid(column=0, row=0)
ttk.Button(frame, text='Test 2', style='My.TButton').grid(column=3, row=3)

p.mainloop()
'''
