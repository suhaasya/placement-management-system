from tkinter import *
from  tkinter import ttk
import ctypes
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import ctypes
import mysql.connector
import os
import sys
sys.path.append(f'{os.getcwd()}')
from configurations import config



# Add your own database name and password here to reflect in the code
mypass = config.MYPASS
mydatabase = config.MYDATABASE
myusername = config.MYUSERNAME

# Database Connection
con = pymysql.connect(
    host="localhost",
    user= myusername,
    password= mypass
)

cur = con.cursor()
cur.execute(f"CREATE DATABASE IF NOT EXISTS {mydatabase}")
cur.execute(f"USE {mydatabase}")

# Enter table names here
companiesTable = "companies"  # companiesTable

cur.execute(f"""
CREATE TABLE IF NOT EXISTS {companiesTable} (
company_id VARCHAR(255) PRIMARY KEY NOT NULL,
company_name VARCHAR(255),
required_cgpa FLOAT,
Email VARCHAR(255),
Phone_No BIGINT
)""");

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


# quality
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def ViewEligibleStudent():
        
    # Add your own database name and password here to reflect in the code
    mypass = config.MYPASS
    mydatabase = config.MYDATABASE
    myusername = config.MYUSERNAME

    # Database Connection
    con = pymysql.connect(
        host="localhost",
        user= myusername,
        password= mypass
    )

    cur = con.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {mydatabase}")
    cur.execute(f"USE {mydatabase}")

    # Enter table names here
    companiesTable = "companies"  # companiesTable

    cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {companiesTable} (
    company_id VARCHAR(255) PRIMARY KEY NOT NULL,
    company_name VARCHAR(255),
    required_cgpa FLOAT,
    Email VARCHAR(255),
    Phone_No BIGINT
    )""");

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
    ws['bg'] = '#FFF4A3'

    

    lb1 = Label(ws, text="Enter CID : ", bg="#FFF4A3", fg='#282A35', font=('Verdana', 12, "bold"))
    lb1.place(relx=0.13, rely=0.3, relheight=0.04)

    inf1 = Entry(ws)
    inf1.place(relx=0.27, rely=0.3, relwidth=0.62, relheight=0.04)

    headingLabel = Label(ws, text="Eligible Students", bg='#FFF4A3', fg='#000000',
                         font=('Verdana', 40, 'bold'))
    headingLabel.place(relx=0.20, rely=0.1)

    view_frame = Frame(ws)
    # view_frame.pack(pady=250)
    view_frame.place(relx=0.025, rely=0.4)

    # scrollbar
    game_scroll = Scrollbar(view_frame, orient='vertical')
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(view_frame, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    viewC = ttk.Treeview(view_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

    viewC.pack()

    game_scroll.config(command=viewC.yview)
    game_scroll.config(command=viewC.xview)




    viewC['columns'] = ('PRN','Name','Branch','email','phone_no',"avg_cgpa")

    viewC.column("#0", width=0,  stretch=NO)
    viewC.column("PRN",anchor=W, width=100)
    viewC.column("Name",anchor=W,width=200)
    viewC.column("Branch",anchor=W,width=200)
    viewC.column("email",anchor=W,width=250)
    viewC.column("phone_no",anchor=W,width=150)
    viewC.column("avg_cgpa",anchor=W,width=100)


    viewC.heading("#0",text="",anchor=W)
    viewC.heading("PRN",text="PRN",anchor=W)
    viewC.heading("Name",text="Name",anchor=W)
    viewC.heading("Branch",text="Branch",anchor=W)
    viewC.heading("email", text="email", anchor=W)
    viewC.heading("phone_no", text="Phone No.", anchor=W)
    viewC.heading("avg_cgpa", text="avg_cgpa", anchor=W)


    def findStudents():
        id = inf1.get()
        getStudent1 = f'''
                    SELECT @required_cgpa := required_cgpa from {companiesTable} where company_id={id};'''
        # getStudent1 = f'''
        #             SELECT @required_cgpa := required_cgpa from companies where company_id={id};'''
        # getStudent3 = f'''select * from student, studentEdu where student.PRN = studentEdu.PRN AND studentEdu.avg_cgpa >= @required_cgpa;'''
        getStudent3 = f'''select * from {studentTable}, {studentEduTable} where {studentTable}.PRN = {studentEduTable}.PRN AND {studentEduTable}.avg_cgpa >= @required_cgpa;'''  
        
        try:
            cur.execute(getStudent1)
            con.commit()
            cur.execute(getStudent3)
            con.commit()
            for i in cur:
                # print(i)
                viewC.insert(parent='', index='end', iid=i, text='', values=(i[0], f"{i[1]} {i[2]}", i[8],i[5],i[4],i[11]))
        except:
            messagebox.showinfo("Failed to fetch files from database")

    viewC.pack()



    submitBtn = Button(ws, text="Search", bg='#059862', fg='#ffffff', command=findStudents)
    submitBtn.place(relx=0.25, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(ws, text="Quit", bg='#059862', fg='#ffffff', command=ws.destroy)
    quitBtn.place(relx=0.50, rely=0.9, relwidth=0.18, relheight=0.08)
    ws.mainloop()

#
# ViewEligibleStudent()