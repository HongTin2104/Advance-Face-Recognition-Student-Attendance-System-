
import customtkinter
from PIL import Image
import os


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        # self.root.config(bg="black")
        self.root.geometry("1530x790+0+0")
        self.root.title("Hệ Thống Nhận Diện Khuôn Mặt")

        # Set customtkinter theme
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
        # Load and convert images to CTkImage
        img = Image.open("Images/sbackground.jpg")
        img = img.resize((525, 140), Image.LANCZOS)
        self.photoimg = customtkinter.CTkImage(light_image=img, size=(525, 140))

        # Place the image in a label
        f_lbl = customtkinter.CTkLabel(self.root, image=self.photoimg, width=525, height=130)
        f_lbl.place(x=0, y=0)

        # Image 2
        img1 = Image.open("Images/sbackground.jpg")
        img1 = img1.resize((525, 140), Image.LANCZOS)
        self.photoimg1 = customtkinter.CTkImage(light_image=img1, size=(525, 140))

        # Place the image in a label
        f_lbl1 = customtkinter.CTkLabel(self.root, image=self.photoimg1, width=525, height=130)
        f_lbl1.place(x=500, y=0)

        # Image 3
        img2 = Image.open("Images/sbackground.jpg")
        img2 = img2.resize((525, 140), Image.LANCZOS)
        self.photoimg2 = customtkinter.CTkImage(light_image=img2, size=(525, 140))

        # Place the image in a label
        f_lbl2 = customtkinter.CTkLabel(self.root, image=self.photoimg2, width=525, height=130)
        f_lbl2.place(x=1000, y=0)

        # Title
        title_lbl = customtkinter.CTkLabel(self.root, text="HỆ THỐNG ĐIỂM DANH SINH VIÊN BẰNG NHẬN DIỆN KHUÔN MẶT", font=("times new roman", 28, "bold"), fg_color="black", text_color="#EE6AA7", width=1530, height=45)
        title_lbl.place(x=0, y=0)

        # Set the button width to be consistent
        button_width = 150
        button_height = 150
        font1 = ('Arial', 12, 'bold')
        # Student button
        imgStudentBtn = Image.open("Images/studentBtn.png")
        imgStudentBtn = imgStudentBtn.resize((button_width, button_height), Image.LANCZOS)
        self.photoimgSB = customtkinter.CTkImage(light_image=imgStudentBtn, size=(button_width, button_height))

        b1 = customtkinter.CTkButton(self.root, image=self.photoimgSB, text="Thông Tin",
                                     compound="top",  # Đặt văn bản phía trên hình ảnh
                                     command=self.open_student_window,
                                     width=button_width, text_color="black", font=font1,height=button_height,fg_color='#EE6AA7')
        b1.place(x=350, y=200)

        # Detect face button
        img5 = Image.open("Images/faceDetector.png")
        img5 = img5.resize((button_width, 150), Image.LANCZOS)
        self.photoimg5 = customtkinter.CTkImage(light_image=img5, size=(button_width, 150))

        b2 = customtkinter.CTkButton(self.root, image=self.photoimg5, text="Nhận Diện", compound="top",
                                     command=self.open_faceRecog_window, font=font1, text_color="black", width=button_width, height=button_height, fg_color='#EE6AA7')
        b2.place(x=650, y=200)

        # Attendance face button
        img6 = Image.open("Images/attendanceFaceBtn.png")
        img6 = img6.resize((button_width, 150), Image.LANCZOS)
        self.photoimg6 = customtkinter.CTkImage(light_image=img6, size=(button_width, 150))

        b3 = customtkinter.CTkButton(self.root, image=self.photoimg6, text="Điểm Danh", compound="top",
                                     command=self.open_attendance_window, font=font1, text_color="black", width=button_width, height=button_height, fg_color='#EE6AA7')
        b3.place(x=950, y=200)

        # Train face button
        img7 = Image.open("Images/trainBtn.png")
        img7 = img7.resize((button_width, 150), Image.LANCZOS)
        self.photoimg7 = customtkinter.CTkImage(light_image=img7, size=(button_width, 150))

        b4 = customtkinter.CTkButton(self.root, image=self.photoimg7, text="Huấn Luyện", compound="top",
                                     command=self.open_train_window, text_color="black", font=font1, width=button_width, height=button_height, fg_color='#EE6AA7')
        b4.place(x=350, y=500)

        # Photos face button
        img9 = Image.open("Images/photosBtn.png")
        img9 = img9.resize((button_width, 150), Image.LANCZOS)
        self.photoimg9 = customtkinter.CTkImage(light_image=img9, size=(button_width, 150))

        b6 = customtkinter.CTkButton(self.root, image=self.photoimg9, text="Hình Ảnh", compound="top",
                                     command=self.open_img, width=button_width, font=font1, text_color="black", height=button_height, fg_color='#EE6AA7')
        b6.place(x=650, y=500)

        # Exit button
        img10 = Image.open("Images/exitBtn.png")
        img10 = img10.resize((button_width, 150), Image.LANCZOS)
        self.photoimg10 = customtkinter.CTkImage(light_image=img10, size=(button_width, 150))

        b7 = customtkinter.CTkButton(self.root, image=self.photoimg10, text="Thoát", compound="top",
                                     command=self.exit_application, font=font1, text_color="black", width=button_width, height=button_height, fg_color='#EE6AA7')
        b7.place(x=950, y=500)

    def open_img(self):
        os.startfile("Data")

    def open_student_window(self):
        self.root.destroy()
        import student
        student.open_student_window()

    def open_train_window(self):
        self.root.destroy()
        import train
        train.open_train_window()

    def open_faceRecog_window(self):
        self.root.destroy()
        import face_recognition
        face_recognition.open_faceRecog_window()

    def open_attendance_window(self):
        self.root.destroy()
        import attendance
        attendance.open_attendance_window()

    def exit_application(self):
        self.root.destroy()

def open_main_window():
    root = customtkinter.CTk()
    app = Face_Recognition_System(root)
    root.mainloop()

if __name__ == '__main__':
    open_main_window()
