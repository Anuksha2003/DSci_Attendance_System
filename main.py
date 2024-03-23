# import cv2
# import face_recognition


# img = cv2.imread("virat.jpeg")
# rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img_encoding = face_recognition.face_encodings(rgb_img)[0]

# img2 = cv2.imread("images/virat-kohli.jpeg")
# rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
# img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

# img3 = cv2.imread("images/abd.jpeg")
# rgb_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
# img_encoding3 = face_recognition.face_encodings(rgb_img3)[0]

# img4 = cv2.imread("images/dhoni.jpeg")
# rgb_img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
# img_encoding4 = face_recognition.face_encodings(rgb_img4)[0]

# img5 = cv2.imread("images/rohit.jpeg")
# rgb_img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)
# img_encoding5 = face_recognition.face_encodings(rgb_img5)[0]


# images_encodings = [img_encoding2, img_encoding3, img_encoding4, img_encoding5]
# images_names = ["Virat Kohli", "AB de Villiers", "MS Dhoni", "Rohit Sharma"]

# for i, encoding in enumerate(images_encodings):
#     result = face_recognition.compare_faces([img_encoding], encoding)
#     if result[0]:
#         print("Name:", images_names[i])


# import cv2
# import face_recognition

# group_img = cv2.imread("virat_rohit.jpeg")
# rgb_group_img = cv2.cvtColor(group_img, cv2.COLOR_BGR2RGB)
# group_encodings = face_recognition.face_encodings(rgb_group_img)


# img2 = cv2.imread("images/virat-kohli.jpeg")
# rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
# img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

# img3 = cv2.imread("images/abd.jpeg")
# rgb_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
# img_encoding3 = face_recognition.face_encodings(rgb_img3)[0]

# img4 = cv2.imread("images/dhoni.jpeg")
# rgb_img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
# img_encoding4 = face_recognition.face_encodings(rgb_img4)[0]

# img5 = cv2.imread("images/rohit.jpeg")
# rgb_img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)
# img_encoding5 = face_recognition.face_encodings(rgb_img5)[0]

# images_encodings = [img_encoding2, img_encoding3, img_encoding4, img_encoding5]
# images_names = ["Virat Kohli", "AB de Villiers", "MS Dhoni", "Rohit Sharma"]

# for group_encoding in group_encodings:
#     for i, encoding in enumerate(images_encodings):
#         result = face_recognition.compare_faces([group_encoding], encoding)
#         if result[0]:
#             print("Name:", images_names[i])
#             break  

# import cv2
# import face_recognition

# group_img = cv2.imread("group.jpeg")
# rgb_group_img = cv2.cvtColor(group_img, cv2.COLOR_BGR2RGB)
# group_encoding = face_recognition.face_encodings(rgb_group_img)


# img2 = cv2.imread("images/virat-kohli.jpeg")
# rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
# img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

# img3 = cv2.imread("images/abd.jpeg")
# rgb_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
# img_encoding3 = face_recognition.face_encodings(rgb_img3)[0]

# img4 = cv2.imread("images/dhoni.jpeg")
# rgb_img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
# img_encoding4 = face_recognition.face_encodings(rgb_img4)[0]

# img5 = cv2.imread("images/rohit.jpeg")
# rgb_img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)
# img_encoding5 = face_recognition.face_encodings(rgb_img5)[0]


# images_encodings = [img_encoding2, img_encoding3, img_encoding4, img_encoding5]
# images_names = ["Virat Kohli", "AB de Villiers", "MS Dhoni", "Rohit Sharma"]


# present_names = []


# for i, encoding in enumerate(images_encodings):
#     for group_enc in group_encoding:
#         result = face_recognition.compare_faces([group_enc], encoding)
#         if result[0]:
#             present_names.append(images_names[i])
#             break  


# with open("group_photo_names.txt", "w") as file:
#     for name in present_names:
#         file.write(name + "\n")

# print("Names of persons present in the group photo have been written to 'group_photo_names.txt'.")



# import cv2
# import face_recognition
# from datetime import datetime


# group_img = cv2.imread("group.jpeg")
# rgb_group_img = cv2.cvtColor(group_img, cv2.COLOR_BGR2RGB)
# group_encoding = face_recognition.face_encodings(rgb_group_img)


# img2 = cv2.imread("images/virat-kohli.jpeg")
# rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
# img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

# img3 = cv2.imread("images/abd.jpeg")
# rgb_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
# img_encoding3 = face_recognition.face_encodings(rgb_img3)[0]

# img4 = cv2.imread("images/dhoni.jpeg")
# rgb_img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
# img_encoding4 = face_recognition.face_encodings(rgb_img4)[0]

# img5 = cv2.imread("images/rohit.jpeg")
# rgb_img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)
# img_encoding5 = face_recognition.face_encodings(rgb_img5)[0]


# images_encodings = [img_encoding2, img_encoding3, img_encoding4, img_encoding5]
# images_names = ["Virat Kohli", "AB de Villiers", "MS Dhoni", "Rohit Sharma"]


# present_names = []


# for i, encoding in enumerate(images_encodings):
#     for group_enc in group_encoding:
#         result = face_recognition.compare_faces([group_enc], encoding)
#         if result[0]:
#             present_names.append(images_names[i])
#             break  

# current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# file_name = "group_photo_names.txt"
# with open(file_name, "a") as file:
#     file.write(f"Date-Time: {current_datetime}\n")
#     for name in present_names:
#         file.write(name + "\n")

# print(f"Names of persons present in the group photo along with the current date have been appended to '{file_name}'.")


import cv2
import face_recognition
from datetime import datetime

def main():
    group_img = cv2.imread("group.jpeg")
    rgb_group_img = cv2.cvtColor(group_img, cv2.COLOR_BGR2RGB)
    group_encoding = face_recognition.face_encodings(rgb_group_img)

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

    present_names = []

    for i, encoding in enumerate(images_encodings):
        for group_enc in group_encoding:
            result = face_recognition.compare_faces([group_enc], encoding)
            if result[0]:
                present_names.append(images_names[i])
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
