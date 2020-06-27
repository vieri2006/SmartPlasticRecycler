from firebase import firebase

SPR = firebase.FirebaseApplication('https://smartplastic-65d5e.firebaseio.com/', None)



download = SPR.get('/MyTestData', None)
print (download)

'''
new_user = 'Ozgur Vatansever'
result = SPR.post('/users', new_user)
print (result)
'''

SPR.delete('/users', None)

'''
while True:
    temperature = int(input("What is the temperature? "))

    data_to_upload = {
        'Temp' : temperature,
        'Name' : "Nic"
    }


    result = SPR.post('/MyTestData/', data_to_upload)

    print (result)
'''
