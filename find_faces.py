import face_recognition
from PIL import Image


image = face_recognition.load_image_file("total/Messi.jpg")
face_locations = face_recognition.face_locations(image)

face_locations[0].show()
