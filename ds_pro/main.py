from flask import Flask, render_template, request
import cv2
import face_recognition
from datetime import datetime
import os
import pandas as pd
from flask import jsonify

REGISTERED_USERS_FILE = "registered_users.txt"
EXCEL_FILE = "attendance.xlsx"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register_page():
    return render_template('registration.html')

@app.route('/mark-attendance')
def mark_attendance_page():
    return render_template('mark_attendance.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error1="No file part")
        
        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', error1="No selected file")

        if file:
            file_path = 'uploads/' + file.filename
            file.save(file_path)

            present_names = check_attendance(file_path)

            if present_names:  
                update_attendance_file(present_names)
                update_excel_sheet(present_names)  # Pass present_names to update_excel_sheet
                return render_template('index.html', success1="Attendance marked successfully")
            else:
                return render_template('index.html', error1="No faces recognized in the uploaded photo")

@app.route('/register-user', methods=['POST'])
def register_user():
    if request.method == 'POST':
        name = request.form['name']
        mis = request.form['mis']
        image = request.files['image']
        if name and mis and image:
            image.save(os.path.join('images', image.filename))
            with open(REGISTERED_USERS_FILE, 'a') as f:
                f.write(f"Name: {name}, MIS: {mis}, Image: {image.filename}\n")
            update_excel_sheet1(name, mis)
            return render_template('registration.html', success2="Registration successful")
        else:
            return render_template('registration.html', error2="Please fill in all fields")

def parse_info_file(info_file):
    image_info = {}
    with open(info_file, 'r') as file:
        for line in file:
            if line.strip():
                parts = line.strip().split(',')
                name = parts[0].split(': ')[1].strip()
                image = parts[2].split(': ')[1].strip()
                image_info[image] = name
    return image_info

def check_attendance(file):
    group_img = cv2.imread(file)
    rgb_group_img = cv2.cvtColor(group_img, cv2.COLOR_BGR2RGB)
    group_encodings = face_recognition.face_encodings(rgb_group_img)

    image_info = parse_info_file(REGISTERED_USERS_FILE)
    images_folder = "images"
    present_names = []

    for group_encoding in group_encodings:
        for image_file, name in image_info.items():
            img_path = os.path.join(images_folder, image_file)
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_encoding = face_recognition.face_encodings(rgb_img)[0]
            
            result = face_recognition.compare_faces([group_encoding], img_encoding)
            if result[0]:
                present_names.append(name)
    return present_names

def update_excel_sheet(present_names):
    df_attendance = pd.read_excel(EXCEL_FILE, dtype=str)
    current_date = pd.to_datetime('today').date().strftime('%Y-%m-%d')
    
    if current_date not in df_attendance.columns:
        df_attendance[current_date] = ''
    
    for name in present_names:
        if name in df_attendance['Name.1'].values:
            df_attendance.loc[df_attendance['Name.1'] == name, current_date] = 'P'
        else:
            df_attendance = df_attendance.append({'Name.1': name, current_date: 'P'}, ignore_index=True)

    df_attendance.to_excel(EXCEL_FILE, index=False)
    print(f"Attendance updated for the current date: {current_date}.")

def update_excel_sheet1(new_name, new_mis):
    df_attendance = pd.read_excel(EXCEL_FILE)

    if 'Name.1' not in df_attendance.columns:
        df_attendance['Name.1'] = ''
    if 'MIS.1' not in df_attendance.columns:
        df_attendance['MIS.1'] = ''

    df_attendance.loc[len(df_attendance), 'Name.1'] = new_name
    df_attendance.loc[len(df_attendance) - 1, 'MIS.1'] = new_mis
    
    df_attendance.to_excel(EXCEL_FILE, index=False)
    print(f"New user '{new_name}' added to the Excel sheet.")

def update_attendance_file(present_names):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = "group_photo_names.txt"
    with open(file_name, "a") as file:
        file.write(f"Date-Time: {current_datetime}\n")
        for name in present_names:
            file.write(name + "\n")

    print(f"Names of persons present in the uploaded photo along with the current date and time have been appended to '{file_name}'.")



@app.route('/show-attendance')
def show_attendance():
    # Read the attendance data from the Excel sheet
    df_attendance = pd.read_excel(EXCEL_FILE)
    
    today_date = pd.to_datetime('today').date().strftime('%Y-%m-%d')
    
    if today_date in df_attendance.columns:
        present_names_today = df_attendance.loc[df_attendance[today_date] == 'P', 'Name.1'].tolist()
    else:
        present_names_today = []
    
    return render_template('attendance.html', today_date=today_date, present_names_today=present_names_today)


if __name__ == "__main__":
    app.run(debug=True)
