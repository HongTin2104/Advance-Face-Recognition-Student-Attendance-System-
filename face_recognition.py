
from time import strftime
from datetime import datetime
from tkinter import *
from tkinter import ttk
import csv
import os
import tkinter
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
import pypyodbc as pyodbc
import cv2

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")
        self.recognized_students = {}
        self.message_box_shown = False

        self.attendance_marked = False  # Flag to check if attendance is marked

        font1 = ('Arial', 12, 'bold')
        self.bg_image = Image.open("Images/background.jpg")  # replace with your image file
        self.bg_image = self.bg_image.resize((1920, 1020),
                                             Image.Resampling.LANCZOS)  # Use Image.Resampling.LANCZOS instead of Image.ANTIALIAS
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tkinter.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, width=1920, height=1020)

        title_lbl = tkinter.Label(self.root, text="NHẬN DIỆN ĐIỂM DANH", font=("times new roman", 28, "bold"),
                                  fg="#EE6AA7")
        title_lbl.place(x=0, y=0, width=2000, height=45)

        back_btn = ctk.CTkButton(self.root, text="Trở Lại", font=('Arial', 16, 'bold'), compound="top",
                                 command=self.open_main_window, width=90, height=36, border_width=0, bg_color='white',
                                 corner_radius=8, fg_color="#EE6AA7", text_color="black", hover_color="white")
        back_btn.place(x=0, y=0)


        b6 = ctk.CTkButton(self.root, text="Nhận Diện", font=font1, compound="top",
                           command=self.face_recog, width=100, height=80, border_width=0,
                           corner_radius=8, fg_color="darkblue", text_color="white", hover_color="black")
        b6.place(x=200, y=400, anchor=tkinter.CENTER)

    def mark_attendance(self, i, r, n, d):
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:%S")

        # Check if current time is after 7:00 AM
        if now.time() > datetime.strptime("07:00:00", "%H:%M:%S").time():
            status = "Tre"
        else:
            status = "Hien Dien"

        # Check if the student has already been recognized today
        if i in self.recognized_students and self.recognized_students[i] == d1:
            return

        with open("Face_Recognition.csv", "r+", newline="\n") as f:
            reader = csv.reader(f)
            rows = list(reader)

            # Check if data for today exists in the CSV
            if any(row[5] == d1 for row in rows):
                return

            writer = csv.writer(f)

            # Write attendance record to CSV
            writer.writerow([i, r, n, d, dtString, d1, status])

            # Update recognized_students dictionary
            self.recognized_students[i] = d1

            # Show success message only if it hasn't been shown before
            if not self.message_box_shown:
                self.message_box_shown = True
                messagebox.showinfo("Thông Báo", "Đã điểm danh thành công!")

    # face recognition
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coords = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=DESKTOP-NJ3K8EH\SQLEXPRESS;'
                    'DATABASE=Face_Recog;'
                    'UID=adminTT;'
                    'PWD=123;'
                    'Trusted_Connection=yes;'
                )

                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Name FROM Students WHERE Student_ID = ?", (id,))
                n = my_cursor.fetchone()
                if n:
                    n = "+".join(n)

                my_cursor.execute("SELECT Class FROM Students WHERE Student_ID = ?", (id,))
                r = my_cursor.fetchone()
                if r:
                    r = "+".join(r)

                my_cursor.execute("SELECT Department FROM Students WHERE Student_ID = ?", (id,))
                d = my_cursor.fetchone()
                if d:
                    d = "+".join(d)

                my_cursor.execute("SELECT Student_ID FROM Students WHERE Student_ID = ?", (id,))
                i = my_cursor.fetchone()
                if i:
                    i = "+".join(map(str, i))

                if confidence > 60:
                    cv2.putText(img, f"MSSV: {i}", (x, y - 100), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Lop: {r}", (x, y - 70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Ten: {n}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Khoa: {d}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Khong Xac Dinh", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coords = [x, y, w, h]
                conn.close()
            return coords

        def recognize(img, clf, faceCascade):
            coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

    def open_main_window(self):
        self.root.destroy()  # Close the window of the student file
        import main  # Import the main file
        main.open_main_window()


def open_faceRecog_window():
    root = ctk.CTk()
    app = Face_Recognition(root)
    root.mainloop()
