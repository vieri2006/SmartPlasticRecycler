import tkinter as tk #import and keep it in their own namespaces
from tkinter import ttk

# Make a subclass or inheritence from tk.Frame
# Frame class is a generic Tk widget

#@param super().__init__() is calling the constructor from super class
#
class HelloView(tk.Frame):
    """A friendly little module"""
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwarsgs)
        
        # Tkinter has its own variable, ex: StringVar, IntVar, DoubleVar, and BooleanVar
        self.name = tk.StringVar()
        self.hello_string = tk.StringVar()
        self.hello_string.set("Hello World") # Set value to Tkinter variable
        
        name_label = ttk.Label(self, text="Name:")
        name_entry = ttk.Entry(self, textvariable=self.name)
        
        # Create a button
        ch_button = ttk.Button(self, text="Change", command=self.on_change)
        
        # Create a label
        hello_label = ttk.Label(self, textvariable=self.hello_string,
            font=("TkDefaulfFont", 64), wraplength=600) # 600 pixels
        
        # Adding widget use grid() geomentry manager not pack() again
        name_label.grid(row=0, column=0, sticky=tk.W)
        name_entry.grid(row=0, column=1, sticky=(tk.W + tk.E))
        ch_button.grid(row=0, column=2, sticky=tk.E)
        hello_label.grid(row=1, column=0, columnspan=3)
                
        # columnconfigure() method is used to make changes to a widget's grid columns       
        self.columnconfigure(1, weight=1)
        
    # To create the callback for ch_button
    def on_change(self):
        if self.name.get().strip():
            self.hello_string.set("Hello " + self.name.get())
        else:
            self.hello_string.set("Hello World")
            
class MyApplication(tk.Tk):
    """Hello World Main Application"""
    
    def __init__(self, *args, **kwargs):
        super().init__(*args, **kwargs)
        self.title("Hello Tkinter")
        self.geometry("800x600")
        self.resizable(width=False, height=False)


HelloView(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
self.columnconfigure(0, weight=1)

if __name__== '__main__':
    app = MyApplication()
    app.mainLoop()
        