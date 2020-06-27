import tkinter as tk
import tkinter.ttk as ttk
import time

root = tk.Tk()
progress = ttk.Progressbar(root, orient='horizontal', length=100, mode='determinate')

def bar():
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 70
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    root.update_idletasks()
    time.sleep(1)
    
progress.pack()
tk.Button(root, text='foo', command=bar).pack()
tk.mainloop