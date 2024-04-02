import cv2
import face_recognition
from datetime import datetime

def main():
    uploaded_img = cv2.imread("group.jpeg")
    rgb_uploaded_img = cv2.cvtColor(uploaded_img, cv2.COLOR_BGR2RGB)
    uploaded_img_encoding = face_recognition.face_encodings(rgb_uploaded_img)

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

    known_encodings = [img_encoding2, img_encoding3, img_encoding4, img_encoding5]
    students = ["Virat Kohli", "AB de Villiers", "MS Dhoni", "Rohit Sharma"]

    present_names = []

    for i, encoding in enumerate(known_encodings):
        for group_enc in uploaded_img_encoding:
            result = face_recognition.compare_faces([group_enc], encoding)
            if result[0]:
                present_names.append(students[i])
                break  
    
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    
    file_name = "group_photo_names.txt"
    with open(file_name, "a") as file:
        file.write(f"Date-Time: {current_datetime}\n")
        for name in present_names:
            file.write(name + "\n")

    print(f"Names of persons present in the group photo along with the current date and time have been appended to '{file_name}'.")

if __name__ == "__main__":
    main()
