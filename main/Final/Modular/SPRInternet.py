### import library firebase
import sys
sys.path.append('/usr/lib/python2.7/dist-packages/') #thonny pakai Python3, python path di term 2.7
from firebase import firebase

### Setup Firebase ###
SPR = firebase.FirebaseApplication('https://smartplastic-65d5e.firebaseio.com/', None)

def makeId(id):
    return ('Alat1/pengguna/' + id)

def get(inetId):
    return SPR.get(inetId, None)

def update(inetId, tipe):
    # Logic to update jumlah botol
    global jumlahBotol
    global saldoAkhir
    global saldoTambahan
    jumlahBotol = str (int(SPR.get(inetId, None)[tipe]) + 1)
    SPR.put(inetId, tipe, jumlahBotol)
    
    # Logic to update Saldo
    if tipe == "botol kecil":
        tipe = "saldo"
        saldoTambahan = "150"
        saldoAkhir = str (int(SPR.get(inetId, None)[tipe]) + 30)
    else :
        tipe = "saldo"
        saldoTambahan = "500"
        saldoAkhir = str (int(SPR.get(inetId, None)[tipe]) + 65)
    SPR.put(inetId, tipe, saldoAkhir)
    
def updateTanggal(inetId, tanggal):
   SPR.put(inetId, "tanggal", tanggal)
   
def liatSaldoTambahan():
    return saldoTambahan

def liatSaldoAkhir():
    return saldoAkhir
    

#----- Fungsi Update -----
#def dataUpdate():