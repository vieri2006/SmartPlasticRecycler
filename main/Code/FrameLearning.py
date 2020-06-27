#----- Import Library -----#
from tkinter import font
from tkinter import messagebox
import tkinter as tk # For root
import tkinter.ttk as ttk # More modern library
from PIL import ImageTk, Image

#--- Firebase
import sys
sys.path.append('/usr/lib/python2.7/dist-packages/') #thonny pakai Python3, python path di term 2.7
from firebase import firebase

#----- Import file lain sebagai Modular -----#
import SPRMethods as M
import SPRRFID as RFID
import SPRInternet as Inet

#import SPRGUI as GUI

#----- Deklarasi Variable Global -----#


# ----- Settings -----#
##Warna
white='#FFFFFF' # variable untuk warna background = putih
green='#A1FCA3' # variable untuk warna hijau

## Build root
blue='#A1FCA5'
root = tk.Tk()
root.title('Smart Plastic Recycler') # GUI Title
root.configure(background='#000000') # White Color background
root.resizable(height=False, width=False) #fullsscreen
root.wm_attributes('-fullscreen','true') #fullscreen

#----------Constants-----------
logo_size=350 #ukuran logo
lcd_width=1280 #ukuran lcd
tengah =1160
lcd_height=800
tebal_garis_pembatas=7 #tebal garis ijo
space_size=100 #ukuran space di kanan untuk estetika, coba ganti tes_spacing dg 'green'
tes_spacing='green' #indikasi tebal spacing
pady_button=6 #padding/jeda tiap kolom/row thd button
padx_button=100
pad_garis=40

# ---------Style-------- #pengaturan ui perlu style, gabisa dikasih argumen langsung di objek
s = ttk.Style()
s.configure('white.TFrame', background='white')
s.configure('green.TFrame', background='green')
s.configure('blue.TFrame', background='blue')
s.configure('button1.TButton', background='white', font='helvetica 22')
# Font untuk judul selamat datang dan terimakasi
font_big = font.Font(family='Calibri', size=64, weight='bold')#define font style

# font untuk intruksi dan button
font_button = font.Font(family='Helvetica', size=32, weight='bold')

# font untuk data
font_data = font.Font(family='Times New Roman', size =32)


#---------Variables---------- #to be used later
v_id = '12312312'
v_nama = 'Nic'
v_saldo = '75000'
v_jumlahBotol = '0'
v_jenisBotol = 'Botol Besar'
v_saldoTambahan = 'Rp 150'
v_saldoAkhir = '18150'

logo_file = tk.PhotoImage(file="logo_resized.png") #import ke py
iconBantuan = tk.PhotoImage(file="iconBantuan.png")
logoKecil = tk.PhotoImage(file="logo60.png")
kosong = tk.PhotoImage(file="isi.png")
pinggir = tk.PhotoImage(file="pinggir.png")

    

# delay
delay=ttk.Entry(root)

#----- Aplikasi Utama -----#
#--------Mainframe-------- #inisiasi frame utama
content=ttk.Frame(root, style='white.TFrame')
content.grid(column=0, row=0)


# --------Frames--------- #frame2 yang dipakai


#logo kecil
frame_logo=ttk.Frame(content, height=lcd_height, width =60, style='white.TFrame')
# height=logo_size,
frame_logo.grid(column=0, row=0, rowspan=7)


#logo awal
frame_awal=ttk.Frame(content, width=tengah, height=60, style='green.TFrame')
frame_awal.grid(column=1, row=0, columnspan=3, sticky='n')
#


#isi
frame_label=ttk.Frame(content, width=tengah, height = lcd_height-60, style='blue.TFrame')
frame_label.grid(column=1, row=1, rowspan=6, columnspan=3, sticky='n')
#

#bantuan
frame_button=ttk.Frame(content, height=lcd_height, width=60, style='white.TFrame')
frame_button.grid(column=4, row=0, rowspan=7)

##
Kecil = ttk.Label(frame_logo,
                  image=logoKecil,
                  background='red',
                  )

Kecil.grid(column=0,row=0)

pinggiran = ttk.Label(frame_logo,
                      image=pinggir,
                      )
pinggiran.grid(column=0,row=1)

bantuu = ttk.Label(frame_button,
                   image=iconBantuan,
                   )
bantuu.grid(column=0,row=0)
pinggiran2 = ttk.Label(frame_button,
                      image=pinggir,
                      )
pinggiran2.grid(column=0,row=1)



root.mainloop()