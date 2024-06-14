from tkcalendar import DateEntry
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk
import pypyodbc as pyodbc
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import csv
from tkinter import filedialog


mydata = []

class Attendance:
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
        self.var_atten_ID = StringVar()
        self.var_atten_class = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_status = StringVar()

        title_lbl = tkinter.Label(text="QUẢN LÝ THÔNG TIN ĐIỂM DANH SINH VIÊN", font=("times new roman", 28, "bold"), fg="#EE6AA7")
        title_lbl.place(x=0, y=0, width=2000, height=45)

        # frame left

        lbl_frame1 = ctk.CTkLabel(main, font=font2, text="Chi Tiết Điểm Danh Sinh Viên:", text_color='#fff')
        lbl_frame1.place(x=25, y=60)
        frame1 = ctk.CTkFrame(main, bg_color='#131314', fg_color='#292933', corner_radius=10, border_width=2, border_color='#EE6AA7',
                              width=700, height=680)
        frame1.place(x=25, y=85)

        # Student ID entry
        lbl_ID = ctk.CTkLabel(frame1, font=font1, text="Mã Sinh Viên:", text_color='#fff')
        lbl_ID.place(x=40, y=70)

        entry_ID = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=170, textvariable=self.var_atten_ID)
        entry_ID.place(x=160, y=70)

        # Student name entry

        lbl_name = ctk.CTkLabel(frame1, font=font1, text="Tên Sinh Viên:", text_color='#fff')
        lbl_name.place(x=370, y=70)

        entry_name = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                border_width=2, width=170, textvariable=self.var_atten_name)
        entry_name.place(x=500, y=70)


        # DoB datetimepicker

        lbl_dob = ctk.CTkLabel(frame1, font=font1, text="Ngày Điểm Danh:", text_color='#fff')
        lbl_dob.place(x=370, y=135)

        entry_dob = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                border_width=2, width=170, textvariable=self.var_atten_date)
        entry_dob.place(x=500, y=135)

        # Email entry

        lbl_email = ctk.CTkLabel(frame1, font=font1, text="Tên Khoa:", text_color='#fff')
        lbl_email.place(x=40, y=135)

        entry_email = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                 border_width=2, width=170, textvariable=self.var_atten_dep)
        entry_email.place(x=160, y=135)


        # Address entry

        lbl_address = ctk.CTkLabel(frame1, font=font1, text="Giờ:", text_color='#fff')
        lbl_address.place(x=40, y=200)

        entry_address = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                 border_width=2, width=170, textvariable=self.var_atten_time)
        entry_address.place(x=160, y=200)

        # Class entry

        lbl_class = ctk.CTkLabel(frame1, font=font1, text="Tên Lớp:", text_color='#fff')
        lbl_class.place(x=370, y=200)

        entry_class = ctk.CTkEntry(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                     border_width=2, width=170, textvariable=self.var_atten_class)
        entry_class.place(x=500, y=200)

        # Department combobox

        optionsD = ["Có Mặt", "Vắng", "Trễ"]

        lbl_depa = ctk.CTkLabel(frame1, font=font1, text="Trạng Thái:", text_color='#fff')
        lbl_depa.place(x=40, y=265)

        cbx_depa = ctk.CTkComboBox(frame1, font=font1, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                     dropdown_hover_color='#B2016C', button_hover_color='#B2016C', width=170,
                                     variable=self.var_atten_status, values=optionsD, state='readonly')
        cbx_depa.set("Trạng thái")
        cbx_depa.place(x=160, y=265)

        # Define labels and frames
        lbl_frame2 = ctk.CTkLabel(root, font=font2, text="Chi Tiết Điểm Danh:", text_color='#fff')
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
        self.AttendanceReportTable = ttk.Treeview(frame2, height=15, show="headings")

        # Define columns
        self.AttendanceReportTable['columns'] = (
            "id", "class", "name", "department", "time", "date", "attendance")

        # Format columns
        self.AttendanceReportTable.column('#0', width=0, stretch=tk.NO)
        self.AttendanceReportTable.column('id', anchor=tk.CENTER, width=120)
        self.AttendanceReportTable.column('class', anchor=tk.CENTER, width=120)
        self.AttendanceReportTable.column('name', anchor=tk.CENTER, width=200)
        self.AttendanceReportTable.column('department', anchor=tk.CENTER, width=100)
        self.AttendanceReportTable.column('time', anchor=tk.CENTER, width=200)
        self.AttendanceReportTable.column('date', anchor=tk.CENTER, width=150)
        self.AttendanceReportTable.column('attendance', anchor=tk.CENTER, width=70)


        # Define headings
        self.AttendanceReportTable.heading('#0', text='', anchor=tk.CENTER)
        self.AttendanceReportTable.heading('id', text='Mã Sinh Viên', anchor=tk.CENTER)
        self.AttendanceReportTable.heading('class', text='Lớp', anchor=tk.CENTER)
        self.AttendanceReportTable.heading('name', text='Tên Sinh Viên', anchor=tk.CENTER)
        self.AttendanceReportTable.heading('department', text='Tên Khoa', anchor=tk.CENTER)
        self.AttendanceReportTable.heading('time', text='Giờ', anchor=tk.CENTER)
        self.AttendanceReportTable.heading('date', text='Ngày', anchor=tk.CENTER)
        self.AttendanceReportTable.heading('attendance', text='Trạng Thái', anchor=tk.CENTER)


        # Add vertical scrollbar
        vsb = ttk.Scrollbar(frame2, orient="vertical", command=self.AttendanceReportTable.yview)
        vsb.place(x=830, y=20, height=330)  # Adjust placement as needed
        self.AttendanceReportTable.configure(yscrollcommand=vsb.set)

        # Add horizontal scrollbar
        hsb = ttk.Scrollbar(frame2, orient="horizontal", command=self.AttendanceReportTable.xview)
        hsb.place(x=20, y=350, width=820)  # Adjust placement as needed
        self.AttendanceReportTable.configure(xscrollcommand=hsb.set)

        # Place the treeview
        self.AttendanceReportTable.place(x=20, y=20, width=820, height=330)

        # Bind the treeview and fetch data
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        # self.fetch_data()

        # buttons

        btn_save = ctk.CTkButton(frame1, command=self.importCsv,font=font1, text_color='#fff', text='Nhập CSV', fg_color='#B2016C',
                                 hover_color='#FF69B4', bg_color='#292933', cursor='hand2', corner_radius=5, width=200)
        btn_save.place(x=145, y=330)

        btn_update = ctk.CTkButton(frame1, command=self.exportCsv,font=font1, text_color='#fff', text='Xuất CSV', fg_color='#B2016C',
                                 hover_color='#FF69B4', bg_color='#292933', cursor='hand2', corner_radius=5, width=200)
        btn_update.place(x=380, y=330)

        btn_takeP = ctk.CTkButton(frame1, command=self.reset_data,font=font1, text_color='#fff', text='Làm Mới', fg_color='#B2016C',
                                  hover_color='#FF69B4', bg_color='#292933', cursor='hand2', corner_radius=5,
                                  width=200)
        btn_takeP.place(x=145, y=360)

        btn_delete = ctk.CTkButton(frame1, font=font1, text_color='#fff', text='Cập Nhật', fg_color='#B2016C',
                                   hover_color='#FF69B4', bg_color='#292933', cursor='hand2', corner_radius=5,
                                   width=200)
        btn_delete.place(x=380, y=360)

        back_btn = ctk.CTkButton(self.root, text="Trở Lại", font=font1, compound="top", bg_color='white',
                                 command=self.open_main_window, width=90, height=37, border_width=0,
                                 corner_radius=8, fg_color="#EE6AA7", text_color="black", hover_color="white")
        back_btn.place(x=0, y=0)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Mở CSV",
                                         filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")], parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # export csv

    def exportCsv(self):
        try:
            # Assume mydata is defined somewhere in your class or program
            if len(mydata) < 1:
                messagebox.showerror("Không có dữ liệu", "Không có dữ liệu để xuất", parent=self.root)
                return False

            # Open the save file dialog
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Lưu CSV",
                filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")],
                defaultextension=".csv",  # Ensure the file is saved with a .csv extension
                parent=self.root
            )

            # Check if the user canceled the save file dialog
            if not fln:
                return

            # Write data to the file
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)

            # Show a message when data is successfully exported
            messagebox.showinfo("Xuất dữ liệu", f"Dữ liệu của bạn đã xuất thành công đến {os.path.basename(fln)}")

        except Exception as e:
            # Show an error message if an exception occurs
            messagebox.showerror("Lỗi", f"Do: {str(e)}", parent=self.root)


    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_ID.set(rows[0])
        self.var_atten_class.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_status.set(rows[6])

    def reset_data(self):

        self.var_atten_ID.set("")
        self.var_atten_class.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("")

    def open_main_window(self):
        self.root.destroy()  # Đóng cửa sổ của file student
        import main  # Import file main
        main.open_main_window()
def open_attendance_window():
    root = ctk.CTk()
    app = Attendance(root)
    root.mainloop()

