import SPRInternet as Inet
import SPRRFID as RFID
import datetime

# get id from RFID
tanggal = datetime.datetime.now().strftime('%d/%m/%Y')
id = str(RFID.checkId())

print(RFID.getId())


# get firebase id
inetId = Inet.makeId(id)

# update data in firebase
Inet.update(inetId, "botol besar")
Inet.updateTanggal(inetId, tanggal)

# check
result = Inet.get(inetId)

print (result)



