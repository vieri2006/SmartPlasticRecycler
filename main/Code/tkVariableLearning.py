import SPRInternet as Inet
import SPRRFID as RFID

# get id from RFID
id = str(RFID.checkId())

# get firebase id
inetId = Inet.makeId(id)

# update data in firebase
Inet.update(inetId, "botol besar")

# check
result = Inet.get(inetId)

print (result)




