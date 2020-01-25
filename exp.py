import face_recognition

img = face_recognition.load_image_file('ekow.jpg')
face_encoding = face_recognition.face_encodings(img)

print(face_encoding[0])