import numpy as np
import os
import tkinter
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import PhotoImage
from tkinter import messagebox
import pypyodbc as pyodbc
import cv2

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")
        font1 = ('Arial', 12, 'bold')
        # Load and set the background image
        self.bg_image = Image.open("Images/background.jpg")  # replace with your image file
        self.bg_image = self.bg_image.resize((1920, 1020),
                                             Image.Resampling.LANCZOS)  # Use Image.Resampling.LANCZOS instead of Image.ANTIALIAS
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tkinter.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, width=1920, height=1020)

        title_lbl = tkinter.Label(self.root, text="HUẤN LUYỆN MÔ HÌNH", font=("times new roman", 28, "bold"),
                                  fg="#EE6AA7")
        title_lbl.place(x=0, y=0, width=2000, height=45)

        back_btn = ctk.CTkButton(self.root, text="Trở Lại", font=('Arial', 16, 'bold'), compound="top",
                                 command=self.open_main_window, width=90, height=36, border_width=0, bg_color='white',
                                 corner_radius=8, fg_color="#EE6AA7", text_color="black", hover_color="white")
        back_btn.place(x=0, y=0)


        b6 = ctk.CTkButton(self.root, text="Huấn Luyện", font=font1,compound="top",
                                 command=self.train_classifier, width=100, height=80, border_width=0,
                                 corner_radius=8, fg_color="darkblue", text_color="white", hover_color="BLACK")
        b6.place(x=200, y=400, anchor=tkinter.CENTER)

    def train_classifier(self):
        data_dir = "Data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  # Gray scale img
            imageNp = np.array(img, 'uint8')

            # ex 29189.12.jpg ==> 29189
            id = int(os.path.split(image)[1].split('.')[0])


            # ex 29189.12.jpg ==> 12
            # id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)

        ids = np.array(ids)

        # train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()  # Modified this line
        clf.train(faces, ids)

        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Thông Báo", "Huấn luyện mô hình thành công!")

    def open_main_window(self):
        self.root.destroy()  # Đóng cửa sổ của file student
        import main  # Import file main
        main.open_main_window()


def open_train_window():
    root = ctk.CTk()
    app = Train(root)
    root.mainloop()