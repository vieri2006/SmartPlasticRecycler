#----- Import Library -----#
from tkinter import font
from tkinter import messagebox
import tkinter as tk # For root
import tkinter.ttk as ttk # More modern library
import datetime
from PIL import ImageTk, Image

#--- Firebase
import sys
sys.path.append('/usr/lib/python2.7/dist-packages/') #thonny pakai Python3, python path di term 2.7
from firebase import firebase

#----- Import file lain sebagai Modular -----#
#import SPRMethods as M
import SPRRFID as RFID
import SPRInternet as Inet

#import SPRGUI as GUI

#----- Deklarasi Variable Global -----#


# ----- Settings -----#
##Warna
white='#FFFFFF' # variable untuk warna background = putih

## Build root
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
space_size=100 #ukuran space di kanan untuk estetika, coba ganti tes_spacing dg 'green'
pady_button=6 #padding/jeda tiap kolom/row thd button
padx_button=80
pad_garis=40

# ---------Style-------- #pengaturan ui perlu style, gabisa dikasih argumen langsung di objek
s = ttk.Style()
s.configure('white.TFrame', background='white')
s.configure('button1.TButton', background='white', font='helvetica 22')
# Font untuk judul selamat datang dan terimakasi
font_big = font.Font(family='Calibri', size=64, weight='bold')#define font style

# font untuk intruksi dan button
font_button = font.Font(family='Helvetica', size=22, weight='bold')

# font untuk data
font_data = font.Font(family='Times New Roman', size =32)


#---------Variables---------- #to be used later
v_id = '12312312'
v_nama = 'Nic'
v_saldo = '75000'
global v_jumlahBotol
v_jumlahBotol = '0'
v_jenisBotol = 'Botol Besar'
v_saldoTambahan = 'Rp 150'
v_saldoAkhir = '18150'

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
frame_awal=ttk.Frame(content, width=tengah, style='white.TFrame')
frame_awal.grid(column=1, row=0, columnspan=3, sticky='n')

#isi
frame_label=ttk.Frame(content, width=tengah, height = lcd_height-60, style='white.TFrame')
frame_label.grid(column=1, row=1, rowspan=6, columnspan=3, sticky='n')

#bantuan
frame_bantuan=ttk.Frame(content, height=lcd_height, width=60, style='white.TFrame')
frame_bantuan.grid(column=4, row=0, rowspan=7)


#---------Masukin Gambar----------
logo_file = tk.PhotoImage(file="logo_resized.png") #import ke py
iconBantuan = tk.PhotoImage(file="iconBantuan.png")
logoKecil = tk.PhotoImage(file="logo60.png")
kosong = tk.PhotoImage(file="isi.png")
pinggir = tk.PhotoImage(file="pinggir.png")
    

## ----- Fungsi -----


### Fungsi Delay
####
'''
def delay1():
    delay11 = delay.after(10000, lambda:[s3_sudah(), label_state2_1.grid_remove(), buttonUdah.grid_remove()])
    return delay11
    
def delay2():
    delay22 = delay.after(10000, lambda:[mulai(), label_state2_1.grid_remove(), buttonUdah.grid_remove()])
    return delay22
'''
def delay3():
    delay33 = delay.after(5000,lambda:[ulang(), mulai()]) 
    return delay33


#Klo tombol bantuan ditekan
def bantu():
    messagebox.showinfo(message='Untuk bantuan silahan hubungi Dartwin 08xxxxxxxxxx')

def mulai():

    global v_jumlahBotol
    v_jumlahBotol = '0'
    
    global logo
    logo = ttk.Label(frame_awal, image=logo_file, background='white')
    logo.grid(column=0,row=0)

    global judul
    judul = ttk.Label(frame_awal, text='Selamat Datang!', font=font_big, background='white')
    judul.grid(column=1,row=0)
    
    global e_mulai
    e_mulai = ttk.Label(frame_label, text="        Silahkan klik tombol mulai\n   lalu tempelkan kartu RFID anda!", width=30,
                        background='white', font=font_button)
    #e_mulai.configure(anchor="center")
    e_mulai.grid(column=1, row=1, pady=pady_button, padx=padx_button)
    
    global button_mulai
    button_mulai=ttk.Button(frame_label, text="Mulai", width=10, style='button1.TButton', command= lambda :[RFID.checkId(),
                                                                                                            s1_mulai()] )
    button_mulai.grid(column=1,row=2, pady=150, padx=padx_button)
    
def s1_mulai():
    v_id = "Id = " + str(RFID.getId())
    global v_namaAja
    v_namaAja = str(Inet.get(Inet.makeId(str(RFID.getId())))["nama"])
    v_nama = "Nama = " + v_namaAja
    v_saldo = "Saldo = " + str(Inet.get(Inet.makeId(str(RFID.getId())))["saldo"])
    
    button_mulai.grid_remove()
    e_mulai.grid_remove()
    logo.grid_remove()
    judul.grid_remove()
    #Ilangin bagian atas
    
    global putih
    putih = ttk.Label(frame_awal,
                      image=kosong)
    putih.grid(column=0, row=0)
    
    
    
    ##--------Frame Logo----------
    global logoLabel
    logoLabel = ttk.Label(frame_logo,
                          image=logoKecil,
                          background='white'
                          )
    logoLabel.grid(column=0,row=0)
    
    global buttonBantuan
    buttonBantuan = ttk.Button(frame_bantuan,
                               image=iconBantuan,
                               style='button1.TButton',
                               command= lambda: bantu())
    buttonBantuan.grid(column=0,row=0)
    
    global pinggiran1
    pinggiran1 = ttk.Label(frame_logo,
                          image=pinggir
                          )
    pinggiran1.grid(column=0,row=1)
    
    global pinggiran2
    pinggiran2 = ttk.Label(frame_bantuan,
                          image=pinggir
                          )
    pinggiran2.grid(column=0,row=1)
    
    ##---------Frame label----------
    global e_apakah
    e_apakah = ttk.Label(frame_label, text ="Apakah datanya benar?", 
                         font=font_button,
                         background='white')
    e_apakah.grid(column=1, row=1, pady=pady_button, padx=padx_button)
    
    global e_id
    e_id = ttk.Label(frame_label, text=v_id, background='white', font=font_data)
    e_id.grid(column=1, row=2, pady=pady_button, padx=padx_button)

    global e_nama
    e_nama = ttk.Label(frame_label, text=v_nama, background='white', font=font_data)
    e_nama.grid(column=1, row=3, pady=pady_button, padx=padx_button)

    global e_saldo
    e_saldo = ttk.Label(frame_label, text=v_saldo, background='white', font=font_data)
    e_saldo.grid(column=1, row=4, pady=pady_button, padx=padx_button)
    
    global buttonKembali
    buttonKembali = ttk.Button(frame_label, text="Salah", style='button1.TButton', command= lambda:[balikKeAwal(), mulai()])
    buttonKembali.grid(column=0,row=5)
    
    global buttonOk
    buttonOk = ttk.Button(frame_label, text = "Benar", style='button1.TButton' , command= lambda : [Inet.update(Inet.makeId(str(RFID.getId())), "botol kecil"), tambahLagi()])
    buttonOk.grid(column=2,row=5)
    
def balikKeAwal():
    logoLabel.grid_remove()
    buttonBantuan.grid_remove()
    e_apakah.grid_remove()
    e_id.grid_remove()
    e_nama.grid_remove()
    e_saldo.grid_remove()
    buttonKembali.grid_remove()
    buttonOk.grid_remove()
    pinggiran1.grid_remove()
    pinggiran2.grid_remove()
    putih.grid_remove()
    
def tambahLagi():
    e_apakah.grid_remove()
    e_id.grid_remove()
    e_nama.grid_remove()
    e_saldo.grid_remove()
    buttonOk.grid_remove()
    buttonKembali.grid_remove()
    
    
    global label_state2_1
    label_state2_1 = ttk.Label(frame_label, text='Silahkan masukkan botol',  background='white', font=font_button,
                               justify='center')
    #, font=font_judul
    label_state2_1.grid(column=1,row=1)
    global label_state2_2
    label_state2_2 = ttk.Label(frame_label, text='ke lubang masuk botol',  background='white', font=font_button,
                               justify='center')
    #, font=font_judul
    label_state2_2.grid(column=1,row=2)
    
    global buttonUdah
    buttonUdah = ttk.Button(frame_label, text = "Udah", style='button1.TButton', command= lambda: tambah())
    # , delay.after_cancel(delay1())
    buttonUdah.grid(column=1,row=3)
    
    #delay1()
    
    
def tambah():
    label_state2_1.grid_remove()
    label_state2_2.grid_remove()
    buttonUdah.grid_remove()
    
    
    
    global v_jumlahBotol
    v_jumlahBotol = str(int(v_jumlahBotol)+1)
    
    global lagi
    lagi = ttk.Label(frame_label, text='Apakah anda masih ingin',
                     background='white', font=font_button)
    lagi.grid(column=1,row=0)
    global jir
    jir = ttk.Label(frame_label, text='memasukkan sampah botol plastik?',
                     background='white', font=font_button)
    jir.grid(column=1,row=1)
    
    global buttonYa
    buttonYa = ttk.Button(frame_label, text = "Ya", style='button1.TButton', command= lambda: loopUWU())
    buttonYa.grid(column=2,row=2)
    
    global buttonGa
    buttonGa = ttk.Button(frame_label, text = "Tidak", style='button1.TButton' ,
                          command= lambda : [Inet.update(Inet.makeId(str(RFID.getId())), "botol kecil"), s3_sudah(), khusus()])
    buttonGa.grid(column=0,row=2)
    
def loopUWU():
    lagi.grid_remove()
    jir.grid_remove()
    buttonYa.grid_remove()
    buttonGa.grid_remove()
    
    global label_state2_1
    label_state2_1 = ttk.Label(frame_label, text='Silahkan masukkan botol',  background='white', font=font_button,
                               justify='center')
    #, font=font_judul
    label_state2_1.grid(column=1,row=1)
    global label_state2_2
    label_state2_2 = ttk.Label(frame_label, text='ke lubang masuk botol',  background='white', font=font_button,
                               justify='center')
    #, font=font_judul
    label_state2_2.grid(column=1,row=2)
    
    global buttonUdah
    buttonUdah = ttk.Button(frame_label, text = "Udah", style='button1.TButton', command= lambda: tambah())
    #, delay.after_cancel(delay2())
    buttonUdah.grid(column=1,row=3)
    
    #delay2()
        
def khusus():
    lagi.grid_remove()
    jir.grid_remove()
    e_apakah.grid_remove()
    e_id.grid_remove()
    e_nama.grid_remove()
    e_saldo.grid_remove()
    label_state2_1.grid_remove()
    label_state2_2.grid_remove()
    buttonYa.grid_remove()
    buttonGa.grid_remove()

def s3_sudah():
    
    
    tanggal = datetime.datetime.now().strftime('%d/%m/%Y')
    global v_jumlahBotol
    v_jumlahBotol = "Jumlah Botol yang dimasukan = " + v_jumlahBotol
    v_jenisBotol = "Jenis Botol = Botol Kecil"
    v_saldoTambahan = "Saldo Tambahan = " + Inet.liatSaldoTambahan()
    v_saldoAkhir = "Saldo Akhir = " + Inet.liatSaldoAkhir()
    
    global e_tanggal
    e_tanggal = ttk.Label(frame_label,
                          text = "Tanggal = " + tanggal,
                          background='white',
                          font=font_data)
    e_tanggal.grid(column=0, row=0, pady=pady_button, padx=padx_button)
    
    global e_banyakBotol
    e_banyakBotol = ttk.Label(frame_label, text=v_jumlahBotol,
                              background='white',font=font_data)
    e_banyakBotol.grid(column=0, row=1, pady=pady_button, padx=padx_button)    

    global e_jenisBotol
    e_jenisBotol = ttk.Label(frame_label, text=v_jenisBotol,
                             background='white', font=font_data)
    e_jenisBotol.grid(column=0, row=2, pady=pady_button, padx=padx_button)

    global e_saldoTambahan
    e_saldoTambahan = ttk.Label(frame_label, text=v_saldoTambahan,
                                background='white', font=font_data)
    e_saldoTambahan.grid(column=0, row=3, pady=pady_button, padx=padx_button)

    global e_saldoAkhir
    e_saldoAkhir = ttk.Label(frame_label, text=v_saldoAkhir,
                             background='white',font=font_data)
    e_saldoAkhir.grid(column=0, row=4, pady=pady_button, padx=padx_button)
 
    global buttonUpdate
    buttonUpdate = ttk.Button(frame_label, text = "Lanjut", style='button1.TButton' , command= lambda : makasi())
    buttonUpdate.grid(column=2,row=5)

def makasi():
    logoLabel.grid_remove()
    e_tanggal.grid_remove()
    buttonBantuan.grid_remove()
    e_banyakBotol.grid_remove()    
    e_jenisBotol.grid_remove()
    e_saldoTambahan.grid_remove()
    e_saldoAkhir.grid_remove()
    buttonUpdate.grid_remove()
    
    global e_makasi
    e_makasi = ttk.Label(frame_label, text="Terimakasih atas kerjasama " + v_namaAja + "\n   semoga dunia menjadi lebih indah =)", font=font_button,
                         background='white')
    e_makasi.grid(column=1, row=1)
    delay3()
    
    global putih2
    putih2 = ttk.Label(frame_label,
                      image=kosong)
    putih2.grid(column=1, row=3)

def ulang():
    e_makasi.grid_remove()
    e_jenisBotol.grid_remove()
    e_saldoTambahan.grid_remove()
    e_saldoAkhir.grid_remove()
    putih.grid_remove()
    putih2.grid_remove()

##----- Event 1 -----#

#frame sisa
    '''
fSisa = lcd_height-logo_size-tebal_garis_pembatas-2*pad_garis-2*pady_button-4*10
frame_button=ttk.Frame(content, width=lcd_width, height=fSisa, style='white.TFrame')
frame_button.grid(column=0, row=6, columnspan=3)
'''
mulai()

# ---------Execution----------

root.mainloop()


