## import
from tkinter import *

## Constant
PROGRAM_NAME = " Footprint Editor "

root = Tk()
root.title(PROGRAM_NAME)


## Add menu bar in the widget
menu_bar = Menu(root)

# Contain
file_menu = Menu(menu_bar, tearoff=0)
# Add file menu items
menu_bar.add_cascade(label='File', menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
# Add eile menu items
menu_bar.add_cascade(label='Edit', menu=edit_menu)

view_menu = Menu(menu_bar, tearoff=0)
# Add eile menu items
menu_bar.add_cascade(label='View', menu=view_menu)

about_menu = Menu(menu_bar, tearoff=0)
# Add eile menu items
menu_bar.add_cascade(label='About', menu=about_menu)

# Add menu to monitor
root.config(menu=menu_bar)

# Add Undo in Edit menu
edit_menu.add_command(label="Undo", accelerator='Ctrl + Z', compound='left')

# Add frame with Color
shortcut_bar = Frame(root, height=25, background='light sea green')
shortcut_bar.pack(expand='no', fill='x')

line_number_bar = Text(root, width=4, padx=3, takefocus=0, border=0, background='khaki', state='disabled', wrap='none')
line_number_bar.pack(side='left', fill='y')

# Add Text Widget and Scrollbar Widget
content_text = Text(root, wrap='word')
content_text.pack(expand='yes', fill='both')
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')


root.mainloop()
