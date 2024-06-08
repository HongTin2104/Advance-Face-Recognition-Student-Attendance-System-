
## Chay Bth
import numpy as np
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pypyodbc as pyodbc
import cv2

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")

        title_lbl = Label(text="TRAIN DATA SET", font=("times new roman", 35, "bold"), fg="pink")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        b6 = Button(self.root, command=self.train_classifier, text="Train data", cursor="hand2", font=("times new roman", 12, "bold"), bg="pink", fg="black")
        b6.place(x=0, y=100, width=1530, height=100)

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
        messagebox.showinfo("Result", "Training datasets completed")




if __name__ == '__main__':
    root = Tk()
    obj = Train(root)
    root.mainloop()
