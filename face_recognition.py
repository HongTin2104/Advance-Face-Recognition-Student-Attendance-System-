import numpy as np
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pypyodbc as pyodbc
import cv2
class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), fg="pink")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        b6 = Button(self.root, command=self.face_recog, text="Train data", cursor="hand2", font=("times new roman", 12, "bold"), bg="pink", fg="black")
        b6.place(x=0, y=100, width=1530, height=100)



    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coords = []


            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                # messagebox.showinfo(str(id))
                conn = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=DESKTOP-NJ3K8EH\SQLEXPRESS;'
                    'DATABASE=Face_Recognition;'
                    'UID=219819;'
                    'PWD=123;'
                    'Trusted_Connection=yes;'
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Name FROM Students WHERE Student_ID = ?", (id,))
                n = my_cursor.fetchone()
                if n:
                    n = "+".join(n)

                my_cursor.execute("SELECT Roll FROM Students WHERE Student_ID = ?", (id,))
                r = my_cursor.fetchone()
                if r:
                    r = "+".join(r)

                my_cursor.execute("SELECT Department FROM Students WHERE Student_ID = ?", (id,))
                d = my_cursor.fetchone()
                if d:
                    d = "+".join(d)

                if confidence > 77:
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coords = [x, y, w, h]
                conn.close()
            return coords

        def recognize(img, clf, faceCascade):
            coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()  # Tạo bộ nhận diện khuôn mặt LBPH
        clf.read("classifier.xml")  # Đọc mô hình đã được huấn luyện

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Nhấn 'Enter' để thoát
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()