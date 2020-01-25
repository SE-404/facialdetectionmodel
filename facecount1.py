from PIL import Image
import face_recognition
import os


#image = face_recognition.load_image_file("./pics/1.jpg")
image = face_recognition.load_image_file("people.jpg")


face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))
#os.system('mkdir "$(date +%a)"')
'''
for face_location in face_locations:
    d=0
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    file_name = 'image_%d.jpg'%d
    pil_image.save(file_name)
    d+=1
'''

for number in range(len(face_locations)):
    face_cap = image
    top, right, bottom, left = face_locations[number]
    face_image = face_cap[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    file_name = './Sat/image_%d.jpg'%number
    pil_image.save(file_name)

