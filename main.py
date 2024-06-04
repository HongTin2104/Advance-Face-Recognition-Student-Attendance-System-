from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")  # Corrected the typo here



        # Load the image 1
        img = Image.open("Images/sbackground.jpg")  # Ensure the path is correct
        img = img.resize((500, 130), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        self.photoimg = ImageTk.PhotoImage(img)

        # Place the image in a label
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Image 2
        img1 = Image.open("Images/sbackground.jpg")  # Ensure the path is correct
        img1 = img1.resize((500, 130), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Place the image in a label
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # Image 3
        img2 = Image.open("Images/sbackground.jpg")  # Ensure the path is correct
        img2 = img2.resize((500, 130), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Place the image in a label
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=500, height=130)

        #title
        title_lbl = Label(text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35,"bold"), fg="pink")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #student button
        imgStudentBtn = Image.open("Images/studentBtn.png")  # Ensure the path is correct
        imgStudentBtn = imgStudentBtn.resize((220, 220), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        self.photoimgSB = ImageTk.PhotoImage(imgStudentBtn)

        b1=Button(image=self.photoimgSB, command=self.open_student_window, cursor="hand2")
        b1.pack()
        b1.place(x=200, y=200, width=150, height=150)

        b1_1=Button(text="Student Details", command=self.open_student_window, cursor="hand2", font=("times new roman", 15, "bold"), bg="pink", fg="white")
        b1_1.pack()

        b1_1.place(x=200, y=340, width=150, height=40)

        #Detect face button
        img5 = Image.open("Images/faceDetector.png")  # Ensure the path is correct
        img5 = img5.resize((220, 220), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(image=self.photoimg5, cursor="hand2")
        b2.place(x=500, y=200, width=150, height=150)

        b2_1 = Button(text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="pink",
                      fg="white")
        b2_1.place(x=500, y=340, width=150, height=40)

        #Attendance face button
        img6 = Image.open("Images/attendanceFaceBtn.png")  # Ensure the path is correct
        img6 = img6.resize((220, 220), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(image=self.photoimg6, cursor="hand2")
        b3.place(x=800, y=200, width=150, height=150)

        b3_1 = Button(text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="pink",
                      fg="white")
        b3_1.place(x=800, y=340, width=150, height=40)

        #Train face button
        img7 = Image.open("Images/attendanceFaceBtn.png")  # Ensure the path is correct
        img7 = img7.resize((220, 220), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(image=self.photoimg7, cursor="hand2")
        b4.place(x=1100, y=200, width=150, height=150)

        b4_1 = Button(text="Train Face", cursor="hand2", font=("times new roman", 15, "bold"), bg="pink",
                      fg="white")
        b4_1.place(x=1100, y=340, width=150, height=40)

        #Train data
        img8 = Image.open("Images/attendanceFaceBtn.png")  # Ensure the path is correct
        img8 = img8.resize((220, 220), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(image=self.photoimg8, cursor="hand2")
        b5.place(x=350, y=500, width=150, height=150)

        b5_1 = Button(text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="pink",
                      fg="white")
        b5_1.place(x=350, y=640, width=150, height=40)


        #Photos face button
        img9 = Image.open("Images/attendanceFaceBtn.png")  # Ensure the path is correct
        img9 = img9.resize((220, 220), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(image=self.photoimg9, command=self.open_img,cursor="hand2")
        b6.place(x=650, y=500, width=150, height=150)

        b6_1 = Button(text="Photos", command=self.open_img, cursor="hand2", font=("times new roman", 15, "bold"), bg="pink",
                      fg="white")
        b6_1.place(x=650, y=640, width=150, height=40)

        # Exit button
        img10 = Image.open("Images/attendanceFaceBtn.png")  # Ensure the path is correct
        img10 = img10.resize((220, 220), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(image=self.photoimg10, cursor="hand2")
        b7.place(x=950, y=500, width=150, height=150)

        b7_1 = Button(text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="pink", fg="white")
        b7_1.place(x=950, y=640, width=150, height=40)


    # open images data
    def open_img(self):
        os.startfile("Data")

    # open student management
    def open_student_window(self):
        self.root.destroy()  # Đóng cửa sổ của file main
        root_student = Tk()  # Tạo một cửa sổ mới cho file student
        obj_student = Student(root_student)
        root_student.mainloop()

if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
