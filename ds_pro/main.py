
# from flask import Flask, render_template, request
# import cv2
# import face_recognition
# from datetime import datetime
# import os
# import pandas as pd
# from openpyxl import load_workbook

# REGISTERED_USERS_FILE = "registered_users.txt"
# info_file = "registered_users.txt"
# EXCEL_FILE = "attendance.xlsx"

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':
#         # Check if the post request has the file part
#         if 'file' not in request.files:
#             return render_template('index.html', error1="No file part")
        
#         file = request.files['file']

#         # If user does not select file, browser also submit an empty part without filename
#         if file.filename == '':
#             return render_template('index.html', error1="No selected file")

#         if file:
#     # Save the uploaded file
#             file_path = 'uploads/' + file.filename
#             file.save(file_path)

#     # Check attendance
#             present_names = check_attendance(file_path)

#             if present_names:  # Check if present_names is not empty
#         # Append attendance to file
#                 update_attendance_file(present_names)
#                 update_excel_sheet(present_names)  # Pass present_names to update_excel_sheet
#                 return render_template('index.html', success1="Attendance marked successfully")
#             else:
#                 return render_template('index.html', error1="No faces recognized in the uploaded photo")


# @app.route('/register', methods=['POST'])
# def register():
#     if request.method == 'POST':
#         name = request.form['name']
#         mis = request.form['mis']
#         image = request.files['image']
#         if name and mis and image:
#             image.save(os.path.join('images', image.filename))
#             with open(REGISTERED_USERS_FILE, 'a') as f:
#                 f.write(f"Name: {name}, MIS: {mis}, Image: {image.filename}\n")
#             # Reload the DataFrame of registered users after adding a new entry
#             df_users = pd.read_csv(REGISTERED_USERS_FILE, sep=',\s*', engine='python', header=None, names=['Name', 'MIS', 'Image'])
#             return render_template('index.html', success2="Registration successful")
#         else:
#             return render_template('index.html', error2="Please fill in all fields")
#     else:
#         return 'Method not allowed'




# def parse_info_file(info_file):
#     image_info = {}
#     with open(info_file, 'r') as file:
#         for line in file:
#             if line.strip():
#                 parts = line.strip().split(',')
#                 name = parts[0].split(': ')[1].strip()
#                 image = parts[2].split(': ')[1].strip()
#                 image_info[image] = name
#     # print("Image Info:", image_info)            
#     return image_info



# def check_attendance(file):
#     group_img = cv2.imread(file)
#     rgb_group_img = cv2.cvtColor(group_img, cv2.COLOR_BGR2RGB)
#     group_encodings = face_recognition.face_encodings(rgb_group_img)

#     image_info = parse_info_file(info_file)

#     images_folder = "images"
#     image_files = os.listdir(images_folder)

#     present_names = []

#     for group_encoding in group_encodings:
#         for image_file in image_files:
#             img_path = os.path.join(images_folder, image_file)
#             img = cv2.imread(img_path)
#             rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#             img_encoding = face_recognition.face_encodings(rgb_img)[0]

#             result = face_recognition.compare_faces([group_encoding], img_encoding)
#             if result[0]:
#                 name = image_info.get(image_file)
#                 # print("Matched Image:", image_file, "Name from image_info:", name)  # Debugging line
#                 if name:
#                     present_names.append(name)

#     # print("Present Names:", present_names)  # Debugging line
#     return present_names


# def update_excel_sheet(present_names):
#     excel_file = "attendance.xlsx"
#     registered_users_file = "registered_users.txt"

#     # Read registered users from file
#     with open(registered_users_file, 'r') as file:
#         lines = file.readlines()

#     # Extract names and MIS from the lines
#     names = []
#     mis_values = []
#     for line in lines:
#         if line.strip():
#             name_parts = line.split(',')[0].split(': ')[1].strip()
#             mis_parts = line.split(',')[1].split(': ')[1].strip()
#             names.append(name_parts)
#             mis_values.append(mis_parts)

#     # Create DataFrame for names and MIS
#     df_attendance = pd.DataFrame({'Name': names, 'MIS': mis_values})

#     # Get current date for the new column
#     current_date = pd.to_datetime('today').date().strftime('%Y-%m-%d')

#     # Read the existing Excel file if it exists
#     try:
#         df_excel = pd.read_excel(excel_file)
#     except FileNotFoundError:
#         df_excel = pd.DataFrame()

#     # Add a new column for the current date if it doesn't exist
#     if current_date not in df_excel.columns:
#         df_excel[current_date] = ''

#     # Mark 'P' in front of each name in present_names array in the particular date column
#     for name in present_names:
#         if name in df_excel['Name'].values:
#             df_excel.loc[df_excel['Name'] == name, current_date] = 'P'
#         else:
#             mis = df_attendance[df_attendance['Name'] == name]['MIS'].values
#             if len(mis) > 0:
#                 mis = mis[0]
#                 df_excel = df_excel.append({'Name': name, 'MIS': mis, current_date: 'P'}, ignore_index=True)

#     # Write DataFrame to Excel
#     with pd.ExcelWriter(excel_file) as writer:
#         df_attendance.to_excel(writer, index=False)
#         df_excel.to_excel(writer, index=False, startcol=len(df_attendance.columns) + 1)

#     print(f"Names and MIS from {registered_users_file} loaded into '{excel_file}'.")

#     print(f"Attendance marked for the current date: {current_date}.")


# def update_attendance_file(present_names):
#     current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     file_name = "group_photo_names.txt"
#     with open(file_name, "a") as file:
#         file.write(f"Date-Time: {current_datetime}\n")
#         for name in present_names:
#             file.write(name + "\n")

#     print(f"Names of persons present in the uploaded photo along with the current date and time have been appended to '{file_name}'.")

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request
import cv2
import face_recognition
from datetime import datetime
import os
import pandas as pd

REGISTERED_USERS_FILE = "registered_users.txt"
EXCEL_FILE = "attendance.xlsx"

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

            if present_names:  # Check if present_names is not empty
                # Append attendance to file
                update_attendance_file(present_names)
                update_excel_sheet(present_names)  # Pass present_names to update_excel_sheet
                return render_template('index.html', success1="Attendance marked successfully")
            else:
                return render_template('index.html', error1="No faces recognized in the uploaded photo")

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        mis = request.form['mis']
        image = request.files['image']
        if name and mis and image:
            image.save(os.path.join('images', image.filename))
            with open(REGISTERED_USERS_FILE, 'a') as f:
                f.write(f"Name: {name}, MIS: {mis}, Image: {image.filename}\n")
            update_excel_sheet1(name, mis)
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
    # Load the Excel file
    df_attendance = pd.read_excel(EXCEL_FILE)

    # Check if the 'Name.1' and 'MIS.1' columns exist, otherwise create them
    if 'Name.1' not in df_attendance.columns:
        df_attendance['Name.1'] = ''
    if 'MIS.1' not in df_attendance.columns:
        df_attendance['MIS.1'] = ''

    # Append the new name and MIS to the 'Name.1' and 'MIS.1' columns respectively
    df_attendance.loc[len(df_attendance), 'Name.1'] = new_name
    df_attendance.loc[len(df_attendance) - 1, 'MIS.1'] = new_mis

    # Write the updated DataFrame back to the Excel file
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

if __name__ == "__main__":
    app.run(debug=True)

