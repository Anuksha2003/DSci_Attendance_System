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

# from flask import Flask, render_template, request
# import cv2
# import face_recognition
# from datetime import datetime

# def main():
#     group_img = cv2.imread("virat-rohit.jpeg")
#     rgb_group_img = cv2.cvtColor(group_img, cv2.COLOR_BGR2RGB)
#     group_encoding = face_recognition.face_encodings(rgb_group_img)

#     img2 = cv2.imread("images/virat-kohli.jpeg")
#     rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
#     img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

#     img3 = cv2.imread("images/abd.jpeg")
#     rgb_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
#     img_encoding3 = face_recognition.face_encodings(rgb_img3)[0]

#     img4 = cv2.imread("images/dhoni.jpeg")
#     rgb_img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
#     img_encoding4 = face_recognition.face_encodings(rgb_img4)[0]

#     img5 = cv2.imread("images/rohit.jpeg")
#     rgb_img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)
#     img_encoding5 = face_recognition.face_encodings(rgb_img5)[0]

#     images_encodings = [img_encoding2, img_encoding3, img_encoding4, img_encoding5]
#     images_names = ["Virat Kohli", "AB de Villiers", "MS Dhoni", "Rohit Sharma"]

#     present_names = []

#     for i, encoding in enumerate(images_encodings):
#         for group_enc in group_encoding:
#             result = face_recognition.compare_faces([group_enc], encoding)
#             if result[0]:
#                 present_names.append(images_names[i])
#                 break  

    
#     current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    
#     file_name = "group_photo_names.txt"
#     with open(file_name, "a") as file:
#         file.write(f"Date-Time: {current_datetime}\n")
#         for name in present_names:
#             file.write(name + "\n")

#     print(f"Names of persons present in the group photo along with the current date and time have been appended to '{file_name}'.")

# if __name__ == "__main__":
#     main()



from flask import Flask, render_template, request
import cv2
import face_recognition
from datetime import datetime
import os


REGISTERED_USERS_FILE = "registered_users.txt"
info_file = "registered_users.txt"


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', error1="No file part")
        
        file = request.files['file']

        # If user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            return render_template('index.html', error1="No selected file")

        if file:
            # Save the uploaded file
            file_path = 'uploads/' + file.filename
            file.save(file_path)

            # Check attendance
            present_names = check_attendance(file_path)

            # Append attendance to file
            update_attendance_file(present_names)

            return render_template('index.html', success1="Attendance marked successfully")

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        mis = request.form['mis']
        image = request.files['image']
        if name and mis and image:
            image.save(os.path.join('images', image.filename))
            with open(REGISTERED_USERS_FILE , 'a') as f:
                f.write(f"\nName: {name}, MIS: {mis}, Image: {image.filename}\n")
            return render_template('index.html', success2="Registration successful")
        else:
            return render_template('index.html', error2="Please fill in all fields")
    else:
        return 'Method not allowed'

# def check_attendance(file):
#     group_img = cv2.imread(file)
#     rgb_group_img = cv2.cvtColor(group_img, cv2.COLOR_BGR2RGB)
#     group_encoding = face_recognition.face_encodings(rgb_group_img)

#     images = {
#         "images/virat-kohli.jpeg": "Virat Kohli",
#         "images/abd.jpeg": "AB de Villiers",
#         "images/dhoni.jpeg": "MS Dhoni",
#         "images/rohit.jpeg": "Rohit Sharma"
#     }

#     present_names = []

#     for image_path, name in images.items():
#         img = cv2.imread(image_path)
#         rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         img_encoding = face_recognition.face_encodings(rgb_img)[0]

#         for group_enc in group_encoding:
#             result = face_recognition.compare_faces([group_enc], img_encoding)
#             if result[0]:
#                 present_names.append(name)
#                 break

#     return present_names

# -----------------best-------
# def check_attendance(file):
#     group_img = cv2.imread(file)
#     rgb_group_img = cv2.cvtColor(group_img, cv2.COLOR_BGR2RGB)
#     group_encodings = face_recognition.face_encodings(rgb_group_img)

#     images_folder = "images"
#     image_files = os.listdir(images_folder)

#     present_names = []

#     for group_encoding in group_encodings:
#         for i, image_file in enumerate(image_files):
#             img_path = os.path.join(images_folder, image_file)
#             img = cv2.imread(img_path)
#             rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#             img_encoding = face_recognition.face_encodings(rgb_img)[0]

#             result = face_recognition.compare_faces([group_encoding], img_encoding)
#             if result[0]:
#                 present_names.append(f"Person {i+1}")

#     return present_names

def parse_info_file(info_file):
    image_info = {}
    with open(info_file, 'r') as file:
        for line in file:
            if line.strip():
                parts = line.strip().split(',')
                name = parts[0].split(': ')[1].strip()
                image = parts[2].split(': ')[1].strip()
                image_info[image] = name
    # print("Image Info:", image_info)            
    return image_info

# def check_attendance(group_image):
#     group_img = cv2.imread(group_image)
#     rgb_group_img = cv2.cvtColor(group_img, cv2.COLOR_BGR2RGB)
#     group_encoding = face_recognition.face_encodings(rgb_group_img)[0]

#     image_info = parse_info_file(info_file)
#     images_folder = "images"
#     image_files = os.listdir(images_folder)

#     present_names = []

#     # Store encodings for all images in the group photo
#     encodings = []
#     for image_file in image_files:
#         img_path = os.path.join(images_folder, image_file)
#         img = cv2.imread(img_path)
#         rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         img_encoding = face_recognition.face_encodings(rgb_img)[0]
#         encodings.append(img_encoding)

#     # Compare encodings with the group encoding
#     for img_encoding, image_file in zip(encodings, image_files):
#         result = face_recognition.compare_faces([group_encoding], img_encoding)
#         if result[0] and image_file in image_info:
#             present_names.append(image_info[image_file])

#     return present_names

def check_attendance(file):
    group_img = cv2.imread(file)
    rgb_group_img = cv2.cvtColor(group_img, cv2.COLOR_BGR2RGB)
    group_encodings = face_recognition.face_encodings(rgb_group_img)

    image_info = parse_info_file(info_file)

    images_folder = "images"
    image_files = os.listdir(images_folder)

    present_names = []

    for group_encoding in group_encodings:
        for image_file in image_files:
            img_path = os.path.join(images_folder, image_file)
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            result = face_recognition.compare_faces([group_encoding], img_encoding)
            if result[0]:
                name = image_info.get(image_file)
                # print("Matched Image:", image_file, "Name from image_info:", name)  # Debugging line
                if name:
                    present_names.append(name)

    # print("Present Names:", present_names)  # Debugging line
    return present_names


def update_attendance_file(present_names):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = "group_photo_names.txt"
    with open(file_name, "a") as file:
        file.write(f"Date-Time: {current_datetime}\n")
        for name in present_names:
            file.write(name + "\n")

    print(f"Names of persons present in the uploaded photo along with the current date and time have been appended to '{file_name}'.")

if __name__ == "__main__":
    app.run(debug=True)
