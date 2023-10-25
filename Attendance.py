import cv2
import face_recognition
import os
import numpy as np
import pandas as pd
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import winsound
import mediapipe as mp
# Create a MediaPipe Face Detection object
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

# Create GUI window
root = tk.Tk()
root.title("Attendance Checker")

def empty_csv():
    with open(Path(__file__).with_name('Attendance.csv'), mode='w') as file:
        file.write('Name,Class,Time,Date\n')

# Menu bar with a file menu
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Empty CSV", command=empty_csv)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# Load and preprocess images
path = Path(__file__).resolve().parent / 'Pe'
images = []
classNames = []
mylist = os.listdir(path)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

# new_image_dir = r'C:\Users\Admin\Documents\CPV\-Smart-Attendance-main\Con meo sua'
# new_images = []
# new_classNames = []

# # Traverse through the subdirectories and load the images
# for subdir, dirs, files in os.walk(new_image_dir):
#     for file in files:
#         file_path = os.path.join(subdir, file)
#         curImg = cv2.imread(file_path)
#         new_images.append(curImg)
#         new_classNames.append(os.path.splitext(file)[0])

# images += new_images
# classNames += new_classNames

def findEncodings(images):
    encodeList = []
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

    for img in images:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_detection.process(imgRGB)

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                        int(bboxC.width * iw), int(bboxC.height * ih)
                x1, y1, width, height = bbox
                x2, y2 = x1 + width, y1 + height
                encoded_face = face_recognition.face_encodings(imgRGB, [(y1, x2, y2, x1)])[0]
                encodeList.append(encoded_face)

    return encodeList

encoded_face_train = findEncodings(images)

# Load CSV content
df = pd.read_csv(Path(__file__).with_name('Attendance.csv'))

def markAttendance(name, class_):
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Extract the unique identifier from the recognized name
    unique_identifier = name  # You may need to modify this to extract the identifier correctly
    
    # Use the unique identifier for attendance marking
    with open(Path(__file__).with_name('Attendance.csv'), mode='a') as file:
        file.write(f'{unique_identifier},{class_},{current_time},{current_date}\n')
    
    tree.insert('', 'end', values=[unique_identifier, class_, current_time, current_date])
    winsound.Beep(500, 200)


# Create canvas widget to display video capture
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Create text widget to display attendance name
attendance_label = tk.Label(root, text="Attendance Checking...", font=("Helvetica", 20))
attendance_label.pack(pady=10)

# Create treeview to display attendance records
tree = ttk.Treeview(root)
tree["columns"] = ("Name", "Class", "Time", "Date")
tree.column("#0", width=50)
tree.column("Name", width=100)
tree.column("Class", width=100)
tree.column("Time", width=100)
tree.column("Date", width=100)
tree.heading("#0", text="Index")
tree.heading("Name", text="Name")
tree.heading("Class", text="Class")
tree.heading("Time", text="Time")
tree.heading("Date", text="Date")
tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create video capture object
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    if not success:
        break

    # Convert the image to RGB format
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect faces using MediaPipe Face Detection
    results = face_detection.process(imgRGB)

    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
            x1, y1, width, height = bbox
            x2, y2 = x1 + width, y1 + height

            # Implement your face recognition logic here using MediaPipe's face recognition capabilities
            # Example:
            encoded_face = face_recognition.face_encodings(imgRGB, [(y1, x2, y2, x1)])[0]

            # Implement the matching and attendance marking logic
            matches = face_recognition.compare_faces(encoded_face_train, encoded_face)
            face_distances = face_recognition.face_distance(encoded_face_train, encoded_face)
            match_index = np.argmin(face_distances)

            if matches[match_index]:
                name_class = classNames[match_index]
                if "_" in name_class:
                    class_ = name_class.split('_')[1]
                    name = name_class.split('_')[0]
                else:
                    class_ = "Unknown"  # Assign a default class value if delimiter is missing
                    name = name_class

                # Draw rectangle around the face
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)

                # Add name label
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)


                # Mark attendance
                markAttendance(name, class_)

    # Convert the image to PIL format
    cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)

    # Create the ImageTk object
    imgtk = ImageTk.PhotoImage(image=img)

    # Display the image on the GUI canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)

    # Update the GUI window
    root.update()
