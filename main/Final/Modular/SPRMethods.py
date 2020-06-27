def changeframe(frame, state):
    if state == True:
        state=False
        return frame.grid_forget()
    else:
        state=True
        return frame.grid()

def show_label(self):
    self.label.lift(self.frame)

def hide_button(event):
    event.widget.grid_remove()
    #self.label.lower(self.frame)

def xprint():
    print("Hello World")
    
# -----Meremukan botol-----
#def remuk():
 
 
# -----Mencek Volume Sisa Wadah-----
#def cekVolume():
    
### Kedepannya keliatannya ini ditaro di SPRGUI.py
#----- Event State 2
    
## -- Remove button function
def s2_ok():
    button_ok.grid_remove()
    button_kembali.grid_remove()
    button_batal.grid_remove()
    button_bantuan.grid_remove()

    