import cv2
import face_recognition


img = cv2.imread("virat.jpeg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

img2 = cv2.imread("images/virat-kohli.jpeg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

img3 = cv2.imread("images/abd.jpeg")
rgb_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img_encoding3 = face_recognition.face_encodings(rgb_img3)[0]

img4 = cv2.imread("images/dhoni.jpeg")
rgb_img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
img_encoding4 = face_recognition.face_encodings(rgb_img4)[0]

img5 = cv2.imread("images/rohit.jpeg")
rgb_img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)
img_encoding5 = face_recognition.face_encodings(rgb_img5)[0]


images_encodings = [img_encoding2, img_encoding3, img_encoding4, img_encoding5]
images_names = ["Virat Kohli", "AB de Villiers", "MS Dhoni", "Rohit Sharma"]

for i, encoding in enumerate(images_encodings):
    result = face_recognition.compare_faces([img_encoding], encoding)
    if result[0]:
        print("Name:", images_names[i])
