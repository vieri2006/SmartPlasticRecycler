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
font_judul = font.Font(family='Helvetica', size=64, weight='bold')#define font style

#--------Mainframe-------- #inisiasi frame utama
content=ttk.Frame(root, style='blue.TFrame')
content.grid(column=0, row=0)

# ---------Variables---------- #to be used later
d_id = '12312312'
d_nama = 'Nic'
d_saldo = '75000'
d_jenisBotol = 'Botol Besar'
d_saldoTambahan = 'Rp 150'
d_saldoAkhir = '75150'

v_id = tk.StringVar()
v_nama = tk.StringVar()
v_saldo = tk.StringVar()
v_jenisBotol = tk.StringVar()
v_saldoTambahan = tk.StringVar()
v_saldoAkhir = tk.StringVar()

# temp
v_id.set("Id = " + d_id)
v_nama.set("Nama = " + d_nama)
v_saldo.set("Saldo = " + d_saldo)

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

#---------Frame Logo----------
'''
logo_ori = Image.open("Logo I-Smart Plastic Recycler-Dartwin-ITB.png")#buat logo sesuai keperluan ukuran
logo_resized = logo_ori.resize((logo_size, logo_size), Image.ANTIALIAS)
logo_resized.save("logo_resized.png")

logo_file = tk.PhotoImage(file="logo_resized.png") #import ke py
logo = ttk.Label(frame_logo, image=logo_file, background='white')
logo.grid(column=0,row=0)
'''

judul = ttk.Label(frame_logo, text='Selamat Datang !!!', font=font_judul, background='white')
judul.grid(column=1,row=0)

spacing=ttk.Frame(frame_logo, width=space_size, style=tes_spacing+'.TFrame')
spacing.grid(column=2, row=0)

# ---------Frame Events----------

##  ---------Frame Events 1----------



##  ---------Frame Events 2----------
### ---------Frame Buttons----------
button_ok=ttk.Button(frame_button, text="OK", width=10, style='button1.TButton')
button_ok.grid(column=0,row=0, pady=pady_button, padx=padx_button)
button_kembali=ttk.Button(frame_button, text="Kembali", width=10, style='button1.TButton')
button_kembali.grid(column=0,row=1, pady=pady_button, padx=padx_button)
button_batal=ttk.Button(frame_button, text="Batal", width=10, style='button1.TButton')
button_batal.grid(column=0,row=2, pady=pady_button, padx=padx_button)
button_bantuan=ttk.Button(frame_button, text="Bantuan", width=10, style='button1.TButton')
button_bantuan.grid(column=0,row=3, pady=pady_button, padx=padx_button)


###---------Frame label----------
e_id = tk.Entry(frame_label, textvariable=v_id, background='blue')
e_id.grid(column=0, row=0, pady=pady_button, padx=padx_button)

e_nama = tk.Entry(frame_label, textvariable=v_nama, background='blue')
e_nama.grid(column=0, row=1, pady=pady_button, padx=padx_button)

e_saldo = tk.Entry(frame_label, textvariable=v_saldo, background='blue')
e_saldo.grid(column=0, row=2, pady=pady_button, padx=padx_button)

label_state2_1 = ttk.Label(frame_label, text='Silahkan masukan botol', background='white')
#, font=font_judul
label_state2_1.grid(column=0,row=3)

###---------Frame Pengisi Space Kosong biar fullscreen----------
spacing=ttk.Frame(content, width=space_size, style=tes_spacing+'.TFrame')
spacing.grid(column=3, row=0, rowspan=4)

tebal_sisa=lcd_height-logo_size-tebal_garis_pembatas-2*pad_garis-2*4*pady_button-4*10
frame_sisa=ttk.Frame(content, width=lcd_width, height=tebal_sisa, style=tes_spacing+'.TFrame')
frame_sisa.grid(column=0, row=4, columnspan=3)


##  ---------Frame Events 3----------
##  ---------Frame Events 4----------

# --------Functions---------

# ---------Execution----------
root.mainloop()


