import datetime
import re
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk
import pypyodbc as pyodbc
import tkinter
import cv2
from tkinter import *
from tkinter import ttk
import tkinter as tk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.config(bg='#161C25')
        # self.root.resizable(False, False)
        self.root.title("Student Management")



        font1 = ('Arial', 16, 'bold')
        font2 = ('Arial', 20, 'bold')

        main = self.root

        # variables
        self.var_dep = StringVar()
        # self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_class = StringVar()
        # self.var_div = StringVar()
        # self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        title_lbl = tkinter.Label(text="HỆ THỐNG QUẢN LÝ SINH VIÊN", font=("times new roman", 28, "bold"), fg="#EE6AA7")
        title_lbl.place(x=0, y=0, width=2000, height=45)

        # frame left

        lbl_frame1 = ctk.CTkLabel(main, font=font2, text="Chi Tiết Sinh Viên:", text_color='#fff')
        lbl_frame1.place(x=25, y=60)
        frame1 = ctk.CTkFrame(main, bg_color='#131314', fg_color='#292933', corner_radius=10, border_width=2, border_color='#EE6AA7',
                              width=700, height=680)
        frame1.place(x=25, y=85)

        # Student ID entry
        lbl_ID = ctk.CTkLabel(frame1, font=font1, text="Mã Sinh Viên:", text_color='#fff')
        lbl_ID.place(x=40, y=70)

        entry_ID = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=170, textvariable=self.var_std_id)
        entry_ID.place(x=160, y=70)

        # Student name entry

        lbl_name = ctk.CTkLabel(frame1, font=font1, text="Tên Sinh Viên:", text_color='#fff')
        lbl_name.place(x=370, y=70)

        entry_name = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                border_width=2, width=170, textvariable=self.var_std_name)
        entry_name.place(x=500, y=70)

        # Gender combobox

        optionsG = ["Nam", "Nữ", "Khác"]

        lbl_gender = ctk.CTkLabel(frame1, font=font1, text="Giới Tính:", text_color='#fff')
        lbl_gender.place(x=40, y=135)

        cbx_gender = ctk.CTkComboBox(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                  dropdown_hover_color='#B2016C', button_hover_color='#B2016C', width=170,
                                     variable=self.var_gender, values=optionsG, state='readonly')
        cbx_gender.set("Chọn Giới Tính")
        cbx_gender.place(x=160, y=135)

        # DoB datetimepicker

        lbl_dob = ctk.CTkLabel(frame1, font=font1, text="Ngày Sinh:", text_color='#fff')
        lbl_dob.place(x=370, y=135)

        entry_dob = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                border_width=2, width=170)
        entry_dob.place(x=500, y=135)

        # Email entry

        lbl_email = ctk.CTkLabel(frame1, font=font1, text="Email:", text_color='#fff')
        lbl_email.place(x=40, y=200)

        entry_email = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                 border_width=2, width=170, textvariable=self.var_email)
        entry_email.place(x=160, y=200)

        # Phone No datetimepicker

        lbl_phone = ctk.CTkLabel(frame1, font=font1, text="Số Điện Thoại:", text_color='#fff')
        lbl_phone.place(x=370, y=200)

        entry_phone = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                border_width=2, width=170, textvariable=self.var_phone)
        entry_phone.place(x=500, y=200)

        # Address entry

        lbl_address = ctk.CTkLabel(frame1, font=font1, text="Địa Chỉ:", text_color='#fff')
        lbl_address.place(x=40, y=265)

        entry_address = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                 border_width=2, width=170, textvariable=self.var_address)
        entry_address.place(x=160, y=265)

        # Teacher name entry

        lbl_teacher = ctk.CTkLabel(frame1, font=font1, text="Tên Giảng Viên:", text_color='#fff')
        lbl_teacher.place(x=370, y=265)

        entry_teacher = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                border_width=2, width=170, textvariable=self.var_teacher)
        entry_teacher.place(x=500, y=265)

        # Class entry

        lbl_class = ctk.CTkLabel(frame1, font=font1, text="Tên Lớp:", text_color='#fff')
        lbl_class.place(x=40, y=330)

        entry_class = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                     border_width=2, width=170, textvariable=self.var_class)
        entry_class.place(x=160, y=330)

        # Department combobox

        optionsD = ["CNTT", "Kinh Tế", "Kỹ Thuật"]

        lbl_depa = ctk.CTkLabel(frame1, font=font1, text="Chọn Tên Khoa:", text_color='#fff')
        lbl_depa.place(x=370, y=330)

        cbx_depa = ctk.CTkComboBox(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                     dropdown_hover_color='#B2016C', button_hover_color='#B2016C', width=170,
                                     variable=self.var_dep, values=optionsD, state='readonly')
        cbx_depa.set("Chọn Tên Khoa")
        cbx_depa.place(x=500, y=330)


        # Year entry

        optionsY = ["20-21", "21-22", "22-23", "23-24", "24-25"]

        lbl_year = ctk.CTkLabel(frame1, font=font1, text="Năm Học:", text_color='#fff')
        lbl_year.place(x=40, y=395)

        cbx_year = ctk.CTkComboBox(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                     dropdown_hover_color='#B2016C', button_hover_color='#B2016C', width=170,
                                     variable=self.var_year, values=optionsY, state='readonly')
        cbx_year.set("Chọn Năm Học")
        cbx_year.place(x=160, y=395)

        # Semester combobox

        optionsK = ["Học Kỳ 1", "Học Kỳ 2", "Học Kỳ 3", "Học Kỳ 4", "Học Kỳ 5", "Học Kỳ 6","Học Kỳ 7", "Học Kỳ 8"]

        lbl_year = ctk.CTkLabel(frame1, font=font1, text="Năm Học:", text_color='#fff')
        lbl_year.place(x=370, y=395)

        cbx_year = ctk.CTkComboBox(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                   dropdown_hover_color='#B2016C', button_hover_color='#B2016C', width=170,
                                   variable=self.var_semester, values=optionsK, state='readonly')
        cbx_year.set("Chọn Học Kỳ")
        cbx_year.place(x=500, y=395)

        # Radio button

        self.var_radio1 = StringVar()

        rdb_p = ctk.CTkRadioButton(main, text="Lấy Ảnh Mẫu", fg_color='#B2016C', hover_color='#B2016C', font=font1,
                                   variable=self.var_radio1, value="Yes")
        rdb_np = ctk.CTkRadioButton(main, text="Không Lấy Ảnh Mẫu", fg_color='#B2016C', hover_color='#B2016C',
                                    font=font1, variable=self.var_radio1, value="No")
        rdb_p.place(x=60, y=550)
        rdb_np.place(x=220, y=550)

        # Define labels and frames
        lbl_frame2 = ctk.CTkLabel(root, font=font2, text="Tìm Kiếm Sinh Viên:", text_color='#fff')
        lbl_frame2.place(x=800, y=60)

        frame2 = ctk.CTkFrame(root, bg_color='#131314', fg_color='#292933', corner_radius=10, border_width=2,
                              border_color='#EE6AA7', width=700, height=680)
        frame2.place(x=800, y=85)

        # Configure style
        style = ttk.Style(frame2)
        style.theme_use('clam')
        style.configure('Treeview', font=font1, foreground='#fff', background='#fff', fieldbackground='#fff')
        style.map('Treeview', background=[('selected', '#EE6AA7')])

        # Create the Treeview widget
        self.tree = ttk.Treeview(frame2, height=15, show="headings")

        # Define columns
        self.tree['columns'] = (
            "Khoa", "Năm Học", "Học Kỳ", "Mã Sinh Viên", "Tên Sinh Viên", "Lớp", "Giới Tính", "Ngày Sinh", "Email",
            "SĐT",
            "Địa Chỉ", "Giáo Viên", "Ảnh Mẫu")

        # Format columns
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('Khoa', anchor=tk.CENTER, width=120)
        self.tree.column('Năm Học', anchor=tk.CENTER, width=120)
        self.tree.column('Học Kỳ', anchor=tk.CENTER, width=120)
        self.tree.column('Mã Sinh Viên', anchor=tk.CENTER, width=100)
        self.tree.column('Tên Sinh Viên', anchor=tk.CENTER, width=200)
        self.tree.column('Lớp', anchor=tk.CENTER, width=150)
        self.tree.column('Giới Tính', anchor=tk.CENTER, width=70)
        self.tree.column('Ngày Sinh', anchor=tk.CENTER, width=100)
        self.tree.column('Email', anchor=tk.W, width=200)
        self.tree.column('SĐT', anchor=tk.CENTER, width=100)
        self.tree.column('Địa Chỉ', anchor=tk.W, width=200)
        self.tree.column('Giáo Viên', anchor=tk.W, width=150)
        self.tree.column('Ảnh Mẫu', anchor=tk.CENTER, width=100)

        # Define headings
        self.tree.heading('#0', text='', anchor=tk.CENTER)
        self.tree.heading('Khoa', text='Khoa', anchor=tk.CENTER)
        self.tree.heading('Năm Học', text='Năm Học', anchor=tk.CENTER)
        self.tree.heading('Học Kỳ', text='Học Kỳ', anchor=tk.CENTER)
        self.tree.heading('Mã Sinh Viên', text='Mã Sinh Viên', anchor=tk.CENTER)
        self.tree.heading('Tên Sinh Viên', text='Tên Sinh Viên', anchor=tk.CENTER)
        self.tree.heading('Lớp', text='Lớp', anchor=tk.CENTER)
        self.tree.heading('Giới Tính', text='Giới Tính', anchor=tk.CENTER)
        self.tree.heading('Ngày Sinh', text='Ngày Sinh', anchor=tk.CENTER)
        self.tree.heading('Email', text='Email', anchor=tk.CENTER)
        self.tree.heading('SĐT', text='SĐT', anchor=tk.CENTER)
        self.tree.heading('Địa Chỉ', text='Địa Chỉ', anchor=tk.CENTER)
        self.tree.heading('Giáo Viên', text='Giáo Viên', anchor=tk.CENTER)
        self.tree.heading('Ảnh Mẫu', text='Ảnh Mẫu', anchor=tk.CENTER)

        # Add vertical scrollbar
        vsb = ttk.Scrollbar(frame2, orient="vertical", command=self.tree.yview)
        vsb.place(x=830, y=20, height=330)  # Adjust placement as needed
        self.tree.configure(yscrollcommand=vsb.set)

        # Add horizontal scrollbar
        hsb = ttk.Scrollbar(frame2, orient="horizontal", command=self.tree.xview)
        hsb.place(x=20, y=350, width=820)  # Adjust placement as needed
        self.tree.configure(xscrollcommand=hsb.set)

        # Place the treeview
        self.tree.place(x=20, y=20, width=820, height=330)

        # Bind the treeview and fetch data
        self.tree.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # buttons

        btn_save = ctk.CTkButton(frame1, font=font1, text_color='#fff', text='Lưu', fg_color='#B2016C', command=self.add_data,
                                 hover_color='#FF69B4', bg_color='#292933', cursor='hand2', corner_radius=5, width=200)
        btn_save.place(x=40, y=525)

        btn_update = ctk.CTkButton(frame1, font=font1, text_color='#fff', text='Cập Nhật', fg_color='#B2016C', command=self.update_data,
                                 hover_color='#FF69B4', bg_color='#292933', cursor='hand2', corner_radius=5, width=200)
        btn_update.place(x=255, y=525)

        btn_delete = ctk.CTkButton(frame1, font=font1, text_color='#fff', text='Xóa', fg_color='#B2016C', command=self.delete_data,
                                   hover_color='#FF69B4', bg_color='#292933', cursor='hand2', corner_radius=5,
                                   width=200)
        btn_delete.place(x=475, y=525)

        btn_takeP = ctk.CTkButton(frame1, font=font1, text_color='#fff', text='Chụp Ảnh', fg_color='#B2016C', command=self.generate_dataset,
                                   hover_color='#FF69B4', bg_color='#292933', cursor='hand2', corner_radius=5,
                                   width=200)
        btn_takeP.place(x=145, y=570)

        btn_updateP = ctk.CTkButton(frame1, font=font1, text_color='#fff', text='Cập Nhật Ảnh', fg_color='#B2016C',
                                   hover_color='#FF69B4', bg_color='#292933', cursor='hand2', corner_radius=5,
                                   width=200)
        btn_updateP.place(x=365, y=570)

        back_btn = Button(command=self.open_main_window, text="Trở Lại", width=18, font=("times new roman", 12, "bold"))
        back_btn = ctk.CTkButton(self.root, text="Trở Lại", font=font1, compound="top", bg_color='white',
                                 command=self.open_main_window, width=90, height=37, border_width=0,
                                 corner_radius=8, fg_color="#EE6AA7", text_color="black", hover_color="white")
        back_btn.place(x=0, y=0)
        # treeview
    def add_data(self):

        if (self.var_dep.get() == "Chọn Khoa" or
                self.var_year.get() == "Chọn Năm" or
                self.var_semester.get() == "Chọn Học Kỳ" or
                self.var_std_name.get() == "" or
                self.var_std_id.get() == "" or
                self.var_gender.get() == "Chọn Giới Tính" or
                self.var_email.get() == "" or
                self.var_phone.get() == "" or
                self.var_address.get() == "" or
                self.var_teacher.get() == "" or
                self.var_radio1.get() == ""):
            messagebox.showerror("Lỗi", "Tất cả các trường là bắt buộc", parent=self.root)
        else:
            # Kiểm tra các ô combobox đã được chọn đúng giá trị
            if ("Chọn" in [self.var_dep.get(), self.var_year.get(), self.var_semester.get(),
                           self.var_gender.get()]):
                messagebox.showerror("Lỗi", "Vui lòng chọn một tùy chọn hợp lệ từ combobox.",
                                     parent=self.root)
                return

            # Kiểm tra định dạng email
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.var_email.get()):
                messagebox.showerror("Lỗi", "Vui lòng nhập địa chỉ email hợp lệ.", parent=self.root)
                return

            # Kiểm tra số điện thoại có 10 chữ số
            if not re.match(r"^[0-9]{10}$", self.var_phone.get()):
                messagebox.showerror("Lỗi", "Vui lòng nhập số điện thoại gồm 10 chữ số.", parent=self.root)
                return

            try:
                conn = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=DESKTOP-NJ3K8EH\SQLEXPRESS;'
                    'DATABASE=Face_Recog;'
                    'UID=adminTT;'
                    'PWD=123;'
                    'Trusted_Connection=yes;'
                )
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into Students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(
                                                                                        self.var_dep.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semester.get(),
                                                                                        self.var_std_id.get(),
                                                                                        self.var_std_name.get(),
                                                                                        self.var_class.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_teacher.get(),
                                                                                        self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Thông Báo", "Lưu Thông Tin Sinh Viên Thành Công!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Lỗi", f"Due To: {str(e)}", parent=self.root)



    def fetch_data(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-NJ3K8EH\SQLEXPRESS;'
            'DATABASE=Face_Recog;'
            'UID=adminTT;'
            'PWD=123;'
            'Trusted_Connection=yes;'
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Students")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.tree.delete(*self.tree.get_children())
            for i in data:
                self.tree.insert("", tk.END, values=i)
            conn.commit()
        conn.close()


    # get cursor

    def get_cursor(self, event = ""):
        cursor_focus = self.tree.focus()
        content = self.tree.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0])
        self.var_year.set(data[1])
        self.var_semester.set(data[2])
        self.var_std_id.set(data[3])
        self.var_std_name.set(data[4])
        self.var_class.set(data[5])
        self.var_gender.set(data[6])
        self.var_dob.set(data[7])
        self.var_email.set(data[8])
        self.var_phone.set(data[9])
        self.var_address.set(data[10])
        self.var_teacher.set(data[11])
        self.var_radio1.set(data[12])


    #update function

    def update_data(self):
        if (self.var_dep.get() == "Chọn Khoa" or
                self.var_year.get() == "Chọn Năm" or
                self.var_semester.get() == "Chọn Học Kỳ" or
                self.var_std_name.get() == "" or
                self.var_std_id.get() == "" or
                self.var_gender.get() == "Chọn Giới Tính" or
                self.var_email.get() == "" or
                self.var_phone.get() == "" or
                self.var_address.get() == "" or
                self.var_teacher.get() == "" or
                self.var_radio1.get() == ""):
            messagebox.showerror("Lỗi", "Tất cả các trường là bắt buộc", parent=self.root)
        else:
            # Kiểm tra các ô combobox đã được chọn đúng giá trị
            if ("Chọn" in [self.var_dep.get(), self.var_year.get(), self.var_semester.get(),
                           self.var_gender.get()]):
                messagebox.showerror("Lỗi", "Vui lòng chọn một tùy chọn hợp lệ từ combobox.",
                                     parent=self.root)
                return

            # Kiểm tra định dạng email
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.var_email.get()):
                messagebox.showerror("Lỗi", "Vui lòng nhập địa chỉ email hợp lệ.", parent=self.root)
                return

            # Kiểm tra số điện thoại có 10 chữ số
            if not re.match(r"^[0-9]{10}$", self.var_phone.get()):
                messagebox.showerror("Lỗi", "Vui lòng nhập số điện thoại gồm 10 chữ số.", parent=self.root)
                return
            try:
                Update = messagebox.askyesno("Thông Báo", "Chắc Chắn Rằng Bạn Muốn Cập Nhật!", parent=self.root)
                if Update > 0:
                    conn = pyodbc.connect(
                        'DRIVER={ODBC Driver 17 for SQL Server};'
                        'SERVER=DESKTOP-NJ3K8EH\SQLEXPRESS;'
                        'DATABASE=Face_Recog;'
                        'UID=adminTT;'
                        'PWD=123;'
                        'Trusted_Connection=yes;'
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "Update Students Set Department=?, Year=?, Semester=?, Name=?, Class=?, Gender=?, DoB=?, Email=?, Phone=?, Address=?, Teacher=?, PhotoSample=? WHERE Student_ID=?",
                        (
                            self.var_dep.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_class.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Thông Báo", "Cập Nhật Thông Tin Sinh Viên Thành Công!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Due To: {str(e)}", parent = self.root )


    # delete function
    def delete_data(self):
        if self.var_std_id.get() == "":
            pass
        else:
            messagebox.showerror("Lỗi", "Tất cả các trường là bắt buộc", parent=self.root)
            try:
                delete = messagebox.askyesno("Xóa Thông Tin Sinh Viên", "Chắc Chắn Rằng Bạn Muốn Xóa", parent = self.root)
                if delete > 0:
                    conn = pyodbc.connect(
                        'DRIVER={ODBC Driver 17 for SQL Server};'
                        'SERVER=DESKTOP-NJ3K8EH\SQLEXPRESS;'
                        'DATABASE=Face_Recog;'
                        'UID=adminTT;'
                        'PWD=123;'
                        'Trusted_Connection=yes;'
                    )
                    my_cursor = conn.cursor()
                    sql = "Delete from Students where Student_ID = ?"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Thông Báo", "Xóa Thành Công!", parent = self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)

    #reset function

    def reset_data(self):
        self.var_dep.set("Chọn Khoa")
        self.var_year.set("Chọn Năm Học")
        self.var_semester.set("Chọn Học Kỳ")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_class.set("")
        self.var_gender.set("Chọn Giới Tính")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # generate data set or take photo samples
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Lỗi", "Cần Điền Đầy Đủ Thông Tin!", parent=self.root)
        else:
            try:
                std_id = self.var_std_id.get()
                conn = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=DESKTOP-NJ3K8EH\SQLEXPRESS;'
                    'DATABASE=Face_Recog;'
                    'UID=adminTT;'
                    'PWD=123;'
                    'Trusted_Connection=yes;'
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from Students")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id += 1
                my_cursor.execute(
                    "Update Students Set Department=?, Year=?, Semester=?, Name=?, Class=?, Gender=?, DoB=?, Email=?, Phone=?, Address=?, Teacher=?, PhotoSample=? WHERE Student_ID=?",
                    (
                        self.var_dep.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_class.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predifiend data on face frontals from opencv

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3,5)
                    # scaling factor = 1.3
                    # minium neighbor = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "Data/" + str(std_id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        # Đặt văn bản ở góc trên bên trái của hình ảnh
                        text_position = (10, 30)
                        cv2.putText(face, str(img_id), text_position, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

                        # cv2.putText(face, str(img_id), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Thêm Ảnh Mẫu Nhận Diện", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Thông Báo", "Thêm Ảnh Thành Công")

            except Exception as e:
                messagebox.showerror("Lỗi", f"Due To: {str(e)}", parent=self.root)

    def open_main_window(self):
        self.root.destroy()  # Đóng cửa sổ của file student
        import main  # Import file main
        main.open_main_window()

def open_student_window():
    root = ctk.CTk()
    app = Student(root)
    root.mainloop()

# if __name__ == "__main__":
#     root = ctk.CTk()
#     app = Student(root)
#     root.mainloop()