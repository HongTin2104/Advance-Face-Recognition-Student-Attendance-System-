from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pypyodbc as pyodbc
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management")  # Corrected the typo here


        # variables

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # Load the image 1
        #
        # img = Image.open("Images/sbackground.jpg")  # Ensure the path is correct
        # img = img.resize((500, 130), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        # self.photoimg = ImageTk.PhotoImage(img)
        #
        # # Place the image in a label
        # f_lbl = Label(self.root, image=self.photoimg)
        # f_lbl.place(x=0, y=0, width=500, height=130)
        #
        # # Image 2
        # img1 = Image.open("Images/sbackground.jpg")  # Ensure the path is correct
        # img1 = img1.resize((500, 130), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        # self.photoimg1 = ImageTk.PhotoImage(img1)
        #
        # # Place the image in a label
        # f_lbl1 = Label(self.root, image=self.photoimg1)
        # f_lbl1.place(x=500, y=0, width=500, height=130)
        #
        # # Image 3
        # img2 = Image.open("Images/sbackground.jpg")  # Ensure the path is correct
        # img2 = img2.resize((500, 130), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        #
        # # Place the image in a label
        # f_lbl2 = Label(self.root, image=self.photoimg2)
        # f_lbl2.place(x=1000, y=0, width=500, height=130)

        # title
        title_lbl = Label(text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), fg="pink")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #main frame
        main_frame=Frame(bd=2,bg="pink")
        main_frame.place(x=0,y=50,width=1600,height=1000)

        #left label frame
        Left_frame=LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE,text="Student Detail", font=("times new roman", 20, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=710)

        # Image 3
        # img2 = Image.open("Images/sbackground.jpg")  # Ensure the path is correct
        # img2 = img2.resize((720, 130), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        #
        # # Place the image in a label
        # f_lbl2 = Label(self.root, image=self.photoimg2)
        # f_lbl2.place(x=18, y=90, width=715, height=130)

        #current course information
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Current course information", font=("times new roman", 15, "bold"))
        current_course_frame.place(x=5,y=130,width=715,height=130)

        #Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep,font=("times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["value"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly", width=20)
        course_combo["value"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #Year

        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly", width=20)
        year_combo["value"] = ("Select Year", "20-21", "21-22", "22-23", "23-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #Semester

        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly", width=20)
        semester_combo["value"] = ("Select Semester", "Semester-1", "Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # #Class student information
        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Class student information", font=("times new roman", 15, "bold"))
        class_student_frame.place(x=5,y=280,width=715, height=370)

        #student ID
        studenID_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        studenID_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        studentID_entry = Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        #student name

        studen_name_label = Label(class_student_frame, text="Student name:", font=("times new roman", 12, "bold"),
                               bg="white")
        studen_name_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        student_name_entry = Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        #class division
        class_div_label = Label(class_student_frame, text="Class division:", font=("times new roman", 12, "bold"),
                                  bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        class_div_entry = Entry(class_student_frame, textvariable=self.var_div, width=20, font=("times new roman", 12, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        #Roll No

        roll_no_label = Label(class_student_frame, text="Roll no:", font=("times new roman", 12, "bold"),
                                  bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        roll_no_entry = Entry(class_student_frame, textvariable=self.var_roll,width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        #Gender

        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly",
                                  width=15)
        gender_combo["value"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        #DoB
        dob_label = Label(class_student_frame, text="DoB:", font=("times new roman", 12, "bold"),
                              bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        dob_entry = Entry(class_student_frame, width=20, textvariable=self.var_dob, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"),
                          bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        email_entry = Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        #Phone No
        phone_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 12, "bold"),
                            bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        phone_entry = Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=10, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"),
                            bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        address_entry = Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        #Teacher Name
        # Phone No
        teacher_name_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"),
                            bg="white")
        teacher_name_label.grid(row=4, column=2, padx=10, pady=10, sticky=W)

        teacher_name_entry = Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_name_entry.grid(row=4, column=3, padx=10, pady=10, sticky=W)

        #radio buttons

        self.var_radio1 = StringVar()
        radioBtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radioBtn1.grid(row=6, column=0, padx=10, pady=10)

        # self.var_radio2 = StringVar()
        radioBtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="No Photo Sample", value="No")
        radioBtn2.grid(row=6, column=1)

        #buttons frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=2, y=260, width=705, height=80)

        save_btn = Button(btn_frame, command=self.add_data,text="Save", width=18,font=("times new roman", 12, "bold"))
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, command=self.update_data,text="Update", width=19, font=("times new roman", 12, "bold"))
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, command=self.delete_data,text="Delete", width=19, font=("times new roman", 12, "bold"))
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, command=self.reset_data,text="Reset", width=18, font=("times new roman", 12, "bold"))
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=2, y=295, width=705, height=50)

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample", width=38, font=("times new roman", 12, "bold"))
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=38, font=("times new roman", 12, "bold"))
        update_photo_btn.grid(row=0, column=2)

        #Right label frame
        right_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE,text="Current Course Information", font=("times new roman", 20, "bold"))
        right_frame.place(x=750, y=10, width=725, height=650)

        # Image 3
        img_right = Image.open("Images/sbackground1.jpg")  # Ensure the path is correct
        img_right = img_right.resize((720, 130), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        # Place the image in a label
        f_lbl3 = Label(right_frame, image=self.photoimg_right)
        f_lbl3.place(x=5, y=-5, width=710, height=130)

        #search frame

        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=80)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="pink", fg="black")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="readonly",
                                      width=10)
        search_combo["value"] = ("Select", "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        search_entry = Entry(search_frame, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        search_btn = Button(search_frame, text="Search", width=13, font=("times new roman", 12, "bold"))
        search_btn.grid(row=0, column=3, padx=10)

        show_all_btn = Button(search_frame, text="Show All", width=13, font=("times new roman", 12, "bold"))
        show_all_btn.grid(row=0, column=4, padx=10)

        #====================table===================

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=260, width=710, height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)



        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DoB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # function decration

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=DESKTOP-NJ3K8EH\SQLEXPRESS;'
                    'DATABASE=Face_Recognition;'
                    'UID=219819;'
                    'PWD=123;'
                    'Trusted_Connection=yes;'
                )
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into Students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semester.get(),
                                                                                        self.var_std_id.get(),
                                                                                        self.var_std_name.get(),
                                                                                        self.var_div.get(),
                                                                                        self.var_roll.get(),
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
                messagebox.showinfo("Success", "Student details has been", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)



    def fetch_data(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-NJ3K8EH\SQLEXPRESS;'
            'DATABASE=Face_Recognition;'
            'UID=219819;'
            'PWD=123;'
            'Trusted_Connection=yes;'
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Students")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    # get cursor

    def get_cursor(self, event = ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])


    #update function

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do u want to update this student details", parent=self.root)
                if Update > 0:
                    conn = pyodbc.connect(
                        'DRIVER={ODBC Driver 17 for SQL Server};'
                        'SERVER=DESKTOP-NJ3K8EH\SQLEXPRESS;'
                        'DATABASE=Face_Recognition;'
                        'UID=219819;'
                        'PWD=123;'
                        'Trusted_Connection=yes;'
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "Update Students Set Department=?, Course=?, Year=?, Semester=?, Name=?, Division=?, Roll=?, Gender=?, DoB=?, Email=?, Phone=?, Address=?, Teacher=?, PhotoSample=? WHERE Student_ID=?",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
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
                messagebox.showinfo("Success", "Student details successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent = self.root )


    # delete function
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do u want to delete this student", parent = self.root)
                if delete > 0:
                    conn = pyodbc.connect(
                        'DRIVER={ODBC Driver 17 for SQL Server};'
                        'SERVER=DESKTOP-NJ3K8EH\SQLEXPRESS;'
                        'DATABASE=Face_Recognition;'
                        'UID=219819;'
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
                messagebox.showinfo("Delete", "Succesully", parent = self.root)
            except Exception as e:
               messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)

    #reset function

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # generate data set or take photo samples
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=DESKTOP-NJ3K8EH\SQLEXPRESS;'
                    'DATABASE=Face_Recognition;'
                    'UID=219819;'
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
                    "Update Students Set Department=?, Course=?, Year=?, Semester=?, Name=?, Division=?, Roll=?, Gender=?, DoB=?, Email=?, Phone=?, Address=?, Teacher=?, PhotoSample=? WHERE Student_ID=?",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() == id + 1
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
                        file_name_path = "Data/User." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        # Đặt văn bản ở góc trên bên trái của hình ảnh
                        text_position = (10, 30)
                        cv2.putText(face, str(img_id), text_position, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

                        # cv2.putText(face, str(img_id), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generate data sets completed ")

            except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()

