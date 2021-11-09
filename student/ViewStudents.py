from tkinter import *
from  tkinter import ttk
import ctypes
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import os
import sys
sys.path.append(f'{os.getcwd()}')
from configurations import config
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)




def ViewStudent():
    # Add your own database name and password here to reflect in the code
    mypass = config.MYPASS
    mydatabase = config.MYDATABASE
    myusername = config.MYUSERNAME

    # Database Connection
    con = mysql.connector.connect(
        host="localhost",
        user= myusername,
        password= mypass
    )

    cur = con.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {mydatabase}")
    cur.execute(f"USE {mydatabase};")

        # Enter Table Names here
    studentTable = "student"  # student table
    studentEduTable = "studentEdu" #student education details table


    cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {studentTable} (
    PRN VARCHAR(255) PRIMARY KEY NOT NULL,
    fname VARCHAR(255),
    lname VARCHAR(255),
    gender VARCHAR(255),
    phone_no BIGINT,
    Email VARCHAR(255),
    DOB VARCHAR(255)
    )""");

    cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {studentEduTable} (
    PRN VARCHAR(255) PRIMARY KEY NOT NULL,
    department VARCHAR(255),
    roll_no VARCHAR(255),
    backlogs INT,
    avg_cgpa FLOAT
    )""");

    ws  = Tk()
    ws.title('ViewCompany')
    ws.geometry('1080x720')
    ws['bg'] = '#D9EEE1'

    

    headingLabel = Label(ws, text="Student Details", bg='#D9EEE1', fg='#000000',
                         font=('Verdana', 40, 'bold'))
    headingLabel.place(relx=0.225, rely=0.1)

    view_frame = Frame(ws)
    view_frame.pack(pady=200)

    # scrollbar
    game_scroll = Scrollbar(view_frame)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(view_frame, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    viewC = ttk.Treeview(view_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

    viewC.pack()

    game_scroll.config(command=viewC.yview)
    game_scroll.config(command=viewC.xview)




    viewC['columns'] = ('PRN', 'Name','Department','Roll_No.', 'Gender', 'Email', "Phone_No.", "Date_of_Birth", "Avg_CGPA", "Backlogs")

    viewC.column("#0", width=0,  stretch=NO)
    viewC.column("PRN",anchor=W, width=80)
    viewC.column("Department",anchor=W, width=130)
    viewC.column("Roll_No.",anchor=W, width=70)
    viewC.column("Name",anchor=W,width=150)
    viewC.column("Gender",anchor=W,width=60)
    viewC.column("Email",anchor=W,width=200)
    viewC.column("Phone_No.", anchor=W, width=90)
    viewC.column("Date_of_Birth", anchor=W, width=130)
    viewC.column("Avg_CGPA", anchor=W, width=80)
    viewC.column("Backlogs", anchor=W, width=70)

    viewC.heading("#0",text="",anchor=W)
    viewC.heading("PRN",text="PRN",anchor=W)
    viewC.heading("Department",text="Department",anchor=W)
    viewC.heading("Roll_No.",text="Roll No.",anchor=W)
    viewC.heading("Name",text="Name",anchor=W)
    viewC.heading("Gender",text="Gender",anchor=W)
    viewC.heading("Email", text="Email", anchor=W)
    viewC.heading("Phone_No.", text="Phone No.", anchor=W)
    viewC.heading("Date_of_Birth", text="Date of Birth", anchor=W)
    viewC.heading("Avg_CGPA", text="Avg CGPA", anchor=W)
    viewC.heading("Backlogs", text="Backlogs", anchor=W)

    getStudent = f"select * from {studentTable}, {studentEduTable} where {studentTable}.PRN = {studentEduTable}.PRN"
  
    try:
      
        cur.execute(getStudent)
        for i in cur:
            # print(i)
            viewC.insert(parent='', index='end', iid=i, text='',values=(i[0],f"{i[1]} {i[2]}",i[8],i[9],i[3],i[5],i[4],i[6],i[11],i[10]))
    except:
        messagebox.showinfo("Failed to fetch files from database")



    viewC.pack()

    quitBtn = Button(ws, text="Quit", bg='#059862', fg='#ffffff', command=ws.destroy, font=('Verdana', 12))
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    ws.mainloop()

# ViewStudent()