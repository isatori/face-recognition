from PIL import Image
import face_recognition

image1 = face_recognition.load_image_file("unknown/Recep_Tayyip_Erdogan_0001.jpg")
image2 = face_recognition.load_image_file("unknown/George_W_Bush_0001.jpg")
face_locations1 = face_recognition.face_locations(image1)
face_locations2 = face_recognition.face_locations(image2)

print("I found {} face(s) in this photograph.".format(len(face_locations1)))
print("I found {} face(s) in this photograph.".format(len(face_locations2)))

for face_location in face_locations1:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image1[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()