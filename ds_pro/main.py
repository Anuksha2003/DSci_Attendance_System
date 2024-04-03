
from flask import Flask, render_template, request
import cv2
import face_recognition
from datetime import datetime
import os
import pandas as pd
from openpyxl import load_workbook

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
            update_excel_sheet(present_names)
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




def update_excel_sheet(present_names):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    group_photo_names = "group_photo_names.txt"

    # Read registered users from file
    registered_users_file = "registered_users.txt"
    df_users = pd.read_csv(registered_users_file, header=None, names=['Name', 'MIS', 'Image'])

    # Check if the Excel file already exists, otherwise create a new one
    excel_file = "attendance.xlsx"
    if not os.path.exists(excel_file):
        df = pd.DataFrame(columns=['Date-Time'])
    else:
        df = pd.read_excel(excel_file)

    # Add new column for current datetime
    df[current_datetime] = ''

    # Mark "P" for present corresponding to the student in the photo
    for name in present_names:
        index = df_users.index[df_users['Name'] == name].tolist()
        if index:
            df.iloc[index[0], df.columns.get_loc(current_datetime)] = 'P'

    # Save to Excel file
    with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a') as writer:
        writer.book = load_workbook(excel_file)
        writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
        df.to_excel(writer, index=False, header=writer.sheets['Sheet1'].dimensions == 'A1')

    print(f"Attendance marked for the uploaded photo. Check '{excel_file}'.")

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
