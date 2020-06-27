from tkinter import *
root = Tk()
root.attributes('-fullscreen', True)
root.configure(background='SteelBlue4')
scrW = root.winfo_screenwidth()
scrH = root.winfo_screenheight()
workwindow = str(1024) + "x" + str(768)+ "+" +str(int((scrW-1024)/2)) + "+" +str(int((scrH-768)/2))
top1 = Toplevel(root, bg="light blue")
top1.geometry(workwindow)
top1.title("Top 1 - Workwindow")
top1.attributes("-topmost", 1)  # make sure top1 is on top to start
root.update()                   # but don't leave it locked in place
top1.attributes("-topmost", 0)  # in case you use lower or lift
#exit button - note: uses grid
b3=Button(root, text="Egress", command=root.destroy)
b3.grid(row=0,column=0,ipadx=10, ipady=10, pady=5, padx=5, sticky = W+N)
#____________________________

def selfdestroy(event):  # using the widget attributes of the event object
    event.widget.destroy()  # this callback destroys a widget

def selfremove(event):   #  this callback removes but saves a widget
    event.widget.grid_remove()

def brecover(self):  #  this callback recovers a removed widget - regrids them
    b3.grid(column=0,row=2,padx=10, pady=10, ipadx=5, ipady=5, sticky=W)
    b4.grid(column=0,row=3,padx=10, pady=10, ipadx=5, ipady=5, sticky=W)

# just for demo, we create a frame to put other stuff in so we can find children
f1=Frame(top1, width=800, height=500, bg="blanched almond", relief=GROOVE)
f1.pack(fill="both", expand= "true")
f1.pack_propagate(False)
# create four almost identical buttons for our demo
b1=Button(f1, width=20, height=2, text= "Click Me & Kill Me 1",bg="gray90")
b1.bind("<1>", selfdestroy) #note we are not sending back anything
b2=Button(f1, width=20, height=2, text= "Click Me & Kill Me 2",bg="gray85")
b2.bind("<1>", selfdestroy)
b3=Button(f1, width=20, height=2, text= "Click Me & Remove Me 3", bg="gray80")
b3.bind("<1>", selfremove)
b4=Button(f1, width=20, height=2, text= "Click Me & Remove Me 4", bg="gray75")
b4.bind("<1>", selfremove)
b1.grid(column=0,row=0,padx=10, pady=10, ipadx=5, ipady=5, sticky=W)
b2.grid(column=0,row=1,padx=10, pady=10, ipadx=5, ipady=5, sticky=W)
b3.grid(column=0,row=2,padx=10, pady=10, ipadx=5, ipady=5, sticky=W)
b4.grid(column=0,row=3,padx=10, pady=10, ipadx=5, ipady=5, sticky=W)

# create a text widget which we will populate later
l1=Text(f1, width=100, height=5, bg="light goldenrod2", wrap=WORD)
l1.grid(column=0,row=4, padx=10, pady=10)

# create a button and bind it to Button-1 so we get event information in callback
b5=Button(f1, width=20, height=2, text= "After Removal-\nRecover 3 & 4", bg="red", fg="white")
b5.bind("<1>", brecover)
b5.grid(column=0, row=10, sticky=SE)

# get a list of our frames child widgets and  post the names in our text widget
kidslist=f1.winfo_children()
l1.insert(END, kidslist)

#____________________________
root.mainloop()
