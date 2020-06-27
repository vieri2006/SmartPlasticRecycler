from tkinter import * # Import Tkinter library into global namespace
from tkinter.ttk import * # imports the ttk or themed Tk widget library

# creates root or master application OBJECT (You should only use 1)
root = Tk()

# Creates a new Label Object to display text or image
#@param root : parent or master widget which have the label widget
#@param text : specifies text will be placed in Label object


# label is an object in the main application window
label = Label(root, text = "Welcome to Smart Plastic Recycler !!!")

# places the new label widget onto its parent widget (SIMPLEST GEOMETRY MANAGER)
label.pack()

# Starts mainevent loop. It is responsible for precessing all the events(
# keystrokes, mouse clicks and it will run until the program is quit
root.mainloop()
