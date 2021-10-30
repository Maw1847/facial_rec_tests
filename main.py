

import face_recognition


ronaldo_image = face_recognition.load_image_file('total/Ronaldo.jpg')
ronaldo_image_encoding = face_recognition.face_encodings(ronaldo_image)[0]

messi_image = face_recognition.load_image_file('total/Messi.jpg')
messi_image_encoding = face_recognition.face_encodings(messi_image)[0]

mbappe_image = face_recognition.load_image_file('total/Mbappe.jpg')
mbappe_image_encoding = face_recognition.face_encodings(mbappe_image)[0]

unknown_image = face_recognition.load_image_file('try/unknow4.jpg')
unkown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

knownfaces = [
ronaldo_image_encoding,
messi_image_encoding,
mbappe_image_encoding
]

results = face_recognition.compare_faces(knownfaces, unkown_image_encoding)
print(results)

if results[0] == True and results[1] == False and results[2]== False:
    print("Ronaldo in !")
elif results[0] == False and results[1] == True and results[2]== False: 
    print("Messi in !")
elif results[0] == False and results[1] == False and results[2]== True: 
    print("Mbappe in !")
else:
    print('Unknown person')

