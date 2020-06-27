# ---------Import----------
import SPRMethods
import SPRRFID
from tkinter import font
import tkinter as tk # For root
import tkinter.ttk as ttk # More modern library
from PIL import ImageTk, Image

#----------Constants-----------
logo_size=350 #ukuran logo
lcd_width=1280 #ukuran lcd
lcd_height=800
tebal_garis_pembatas=7 #tebal garis ijo
space_size=100 #ukuran space di kanan untuk estetika, coba ganti tes_spacing dg 'green'
tes_spacing='green' #indikasi tebal spacing
pady_button=6 #padding/jeda tiap kolom/row thd button
padx_button=100
pad_garis=40


# Make Frame
# ---------Settings--------
white='#FFFFFF' # variable untuk warna background = putih
green='#A1FCA3' # variable untuk warna hijau
blue='#A1FCA5' 
root = tk.Tk()
root.title('Smart Plastic Recycler') # GUI Title
root.configure(background='#000000') # White Color background
root.resizable(height=False, width=False) #fullsscreen
root.wm_attributes('-fullscreen','true') #fullscreen

# ---------Style-------- #pengaturan ui perlu style, gabisa dikasih argumen langsung di objek
s = ttk.Style()
s.configure('white.TFrame', background='white')
s.configure('green.TFrame', background='green')
s.configure('blue.TFrame', background='blue')
s.configure('button1.TButton', background='white', font='helvetica 22')
font_judul = font.Font(family='Helvetica', size=32)#define font style

# ---- Variable ----
res = tk.StringVar()

# Testing Change Frame
#--------Mainframe-------- #inisiasi frame utama
content=ttk.Frame(root, style='blue.TFrame')
content.grid(column=0, row=0)

# --------Frames--------- #frame2 yang dipakai

    #logo
frame_logo=ttk.Frame(content, width=lcd_width, height=logo_size, style='white.TFrame')
frame_logo.grid(column=0, row=0, columnspan=3)

    #garis ijo pembatas
frame_garis=ttk.Frame(content, width=lcd_width, height=tebal_garis_pembatas, style='green.TFrame')
frame_garis.grid(column=0, row=1, columnspan=3, pady=pad_garis)

    #button dan keterangan scan ktp
frame_button=ttk.Frame(content, width=420, height=lcd_height-tebal_garis_pembatas-logo_size, style='white.TFrame')
frame_button.grid(column=0, row=2, columnspan=1)

    #label di kanan
frame_label=ttk.Frame(content, width=lcd_width-420, height=lcd_height-tebal_garis_pembatas-logo_size, style='green.TFrame')
frame_label.grid(column=1, row=2, columnspan=2)

###---------Frame Pengisi Space Kosong biar fullscreen----------
spacing=ttk.Frame(content, width=space_size, style=tes_spacing+'.TFrame')
spacing.grid(column=3, row=0, rowspan=4)

tebal_sisa=lcd_height-logo_size-tebal_garis_pembatas-2*pad_garis-2*4*pady_button-4*10
frame_sisa=ttk.Frame(content, width=lcd_width, height=tebal_sisa, style=tes_spacing+'.TFrame')
frame_sisa.grid(column=0, row=4, columnspan=3)

# Button ganti frame

satu = ttk.Label(frame_label, text='satu', font=font_judul, background='white')
satu.grid(column=1,row=2, padx=padx_button)

biru = tk.Entry(frame_label, textvariable=res, background='blue')
biru.grid(column=1, row=2, pady=pady_button, padx=padx_button)

def merah():
    res.set("merah")    


button_checkRFID=ttk.Button(frame_label, text="bobok", width=20, style='button1.TButton', command=merah)
#lambda :bobok()

button_checkRFID.grid(column=0, row=2, pady=pady_button, padx=padx_button)

button_checkRFID=ttk.Button(frame_label, text="bangun", width=20, style='button1.TButton')
button_checkRFID.grid(column=0, row=3, pady=pady_button, padx=padx_button)




# ---------Execution----------
root.mainloop()

