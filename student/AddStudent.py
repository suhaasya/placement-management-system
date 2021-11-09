from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import ctypes
import csv
from tkinter import *
from tkinter import filedialog
import os
import sys
sys.path.append(f'{os.getcwd()}')
from configurations import config
from data.randomDate import *


ctypes.windll.shcore.SetProcessDpiAwareness(1)


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
cur.execute(f"USE {mydatabase}")

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

def importData():
    rows = []
    def openFile():
        filepath = filedialog.askopenfilename()
        file = open(filepath)
        csvreader = csv.reader(file)
        err = False;
        for row in csvreader:
                rows.append(row)
                # insertStudents = "insert into " + studentTable + " values('" + row[0] + "','" + row[1] + "','" + row[2] + "','" + "male" + "','" + (row[6]) + "','" + row[5] + "','" + "1 January 2001" + "')"
                insertStudents = f"insert into {studentTable} values('{row[0]}','{row[1]}','{row[2]}','{row[9]}',{row[6]},'{row[5]}','{randomDate()}')"
                # insertScores = "insert into " + studentEduTable + " values('" + row[0] + "','" + row[7] + "','" + row[3] + "','" + 0 + "','" + float(row[4]) + "')"
                insertScores = f"insert into {studentEduTable} values('{row[0]}','{row[7]}','{row[3]}',0,{row[4]})"
                # print(insertStudents)
                # print(insertScores)
                try:
                    cur.execute(insertStudents)
                    # print("suhas")
                    con.commit()
                    # print("suhas")
                    cur.execute(insertScores)
                    # print("suhas")
                    con.commit()
                    # print("suhas")
                    print('Success', "Student details added successfully")
                except:
                    err=True
                    print("Error", "Can't add data into Database Data Already Added")
                    messagebox.showinfo("Error", "Can't add data into Database Data Already Added")
                    break
        # print(rows)
        if(not err):
            print(err)
            messagebox.showinfo('Success', "Student details added successfully")
        
        file.close()
        window.destroy()

    window = Tk()
    button = Button(window, text="select csv file", command=openFile)
    button.pack(padx=100,pady=10)
    window.mainloop()


def studentRegister():
    PRN = stdInfo1.get()
    fname = stdInfo2.get()
    fname = fname.capitalize()

    lname = stdInfo3.get()
    lname = lname.capitalize()

    gender = str(defaultGender.get())
    DOB = f"{defaultDate.get()} {defaultMonth.get()} {defaultYear.get()}"
    phone_no = stdInfoPno.get()
    Email = stdInfoEmail.get()
    Email = Email.lower()

    department = defaultDepartment.get()
    roll_no = stdInfo11.get()
    backlogs = str(defaultBacklog.get())
    avg_cgpa = stdInfo13.get()

    insertStudents = "insert into " + studentTable + " values('" + PRN + "','" + fname + "','" + lname + "','" + gender + "','" + phone_no + "','" + Email + "','" + DOB + "')"
    insertScores = "insert into " + studentEduTable + " values('" + PRN + "','" + department + "','" + roll_no + "','" + backlogs + "','" + avg_cgpa + "')"
    # print(insertStudents)
    # print(insertScores)
    try:
        cur.execute(insertStudents)
        con.commit()
        cur.execute(insertScores)
        con.commit()
        messagebox.showinfo('Success', "Student details added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")




    root.destroy()


def addStudents():
    global stdInfo1, stdInfo2, stdInfo3, stdInfo4, stdInfo5, stdInfo7,stdInfo10,stdInfo11,stdInfo12,stdInfo13,stdInfoPno,stdInfoEmail, Canvas1, con, cur, studentTable, root, studentEduTable, defaultGender,defaultDate,defaultMonth,defaultYear,defaultDepartment,defaultBacklog

    root = Tk()
    root.title("PM Tool")
    root.geometry("1080x720")

    

    


    Canvas1 = Canvas(root)

    Canvas1.config(bg="#D9EEE1")
    Canvas1.pack(expand=True, fill=BOTH)

    headingLabel = Label(root, text="Add Student Details", bg='#D9EEE1', fg='#000000',
                         font=('Verdana', 40, 'bold'))
    headingLabel.place(relx=0.18, rely=0.1)

    # student ID
    lb1 = Label(root, text="PRN : ",bg="#D9EEE1", fg='#282A35',font=('Verdana', 12,"bold"))
    lb1.place(relx=0.14, rely=0.3, relheight=0.04)

    stdInfo1 = Entry(root)
    stdInfo1.place(relx=0.28, rely=0.3, relwidth=0.59, relheight=0.04)

    # first name
    lb2 = Label(root, text="First Name : ",bg="#D9EEE1", fg='#282A35',font=('Verdana', 12,"bold"))
    lb2.place(relx=0.14, rely=0.35, relheight=0.04)

    stdInfo2 = Entry(root)
    stdInfo2.place(relx=0.28, rely=0.35, relwidth=0.22, relheight=0.04)

    # last name
    lb3 = Label(root, text="Last Name : ",bg="#D9EEE1", fg='#282A35',font=('Verdana', 12,"bold"))
    lb3.place(relx=0.5, rely=0.35, relheight=0.04)

    stdInfo3 = Entry(root)
    stdInfo3.place(relx=0.64, rely=0.35, relwidth=0.23, relheight=0.04)

    # gender
    lb4 = Label(root, text="Gender : ",bg="#D9EEE1", fg='#282A35',font=('Verdana', 12,"bold"))
    lb4.place(relx=0.14, rely=0.40, relheight=0.04)

    defaultGender = StringVar()
    defaultGender.set("Select Your Gender")
    stdInfo4 = OptionMenu(root, defaultGender, "Male", "Female", "LGBTQ")
    stdInfo4.pack()
    stdInfo4.place(relx=0.28, rely=0.40, relwidth=0.18, relheight=0.04)

    #date of birth

    lb5 = Label(root, text="DOB : ",bg="#D9EEE1", fg='#282A35',font=('Verdana', 12,"bold"))
    lb5.place(relx=0.5, rely=0.40, relheight=0.04)

    defaultDate = StringVar()
    defaultDate.set("date")
    date =  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    stdInfo5 = OptionMenu(root, defaultDate, *date)
    stdInfo5.pack()
    stdInfo5.place(relx=0.61, rely=0.40, relwidth=0.07, relheight=0.04)

    defaultMonth = StringVar()
    defaultMonth.set("month")
    month = ['January', 'February','March','April','May','June','July','August','Semptember','November','December']
    stdInfo6 = OptionMenu(root, defaultMonth, *month)
    stdInfo6.pack()
    stdInfo6.place(relx=0.68, rely=0.40, relwidth=0.12, relheight=0.04)

    defaultYear = StringVar()
    defaultYear.set("year")
    year = [1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005]
    stdInfo7 = OptionMenu(root, defaultYear, *year)
    stdInfo7.pack()
    stdInfo7.place(relx=0.8, rely=0.40, relwidth=0.07, relheight=0.04)

    # Phone No.
    lbpno = Label(root, text="Phone No. : ",bg="#D9EEE1", fg='#282A35',font=('Verdana', 12,"bold"))
    lbpno.place(relx=0.14, rely=0.45, relheight=0.04)

    stdInfoPno = Entry(root)
    stdInfoPno.place(relx=0.28, rely=0.45, relwidth=0.22, relheight=0.04)

    # last name
    lbEmail = Label(root, text="Email : ",bg="#D9EEE1", fg='#282A40',font=('Verdana', 12,"bold"))
    lbEmail.place(relx=0.5, rely=0.45, relheight=0.04)

    stdInfoEmail = Entry(root)
    stdInfoEmail.place(relx=0.64, rely=0.45, relwidth=0.23, relheight=0.04)

    # educational details
    lb8 = Label(root, text="Educational details", bg="#D9EEE1", fg='#282A35', font=('Verdana', 12, "bold"))
    lb8.place(relx=0.14, rely=0.55, relheight=0.04)

    
    # department
    
    lb10 = Label(root, text="Department : ",bg="#D9EEE1", fg='#282A35',font=('Verdana', 12,"bold"))
    lb10.place(relx=0.14, rely=0.60, relheight=0.04)
    defaultDepartment = StringVar()
    defaultDepartment.set("Select Department")
    department = ["Computer Science", "Information Technology", "Electronics & Tele.","Mechanical Engineering","Civil Engineering","Bio-Technology","Chemical Engineering"]
    stdInfo10 = OptionMenu(root, defaultDepartment, *department )
    stdInfo10.pack()
    stdInfo10.place(relx=0.28, rely=0.60, relwidth=0.22, relheight=0.04)

    # rollno
    lb11 = Label(root, text="Roll No : ",bg="#D9EEE1", fg='#282A35',font=('Verdana', 12,"bold"))
    lb11.place(relx=0.5, rely=0.60, relheight=0.04)

    stdInfo11 = Entry(root)
    stdInfo11.place(relx=0.64, rely=0.60, relwidth=0.23, relheight=0.04)

    # backlogs
    lb12 = Label(root, text="Backlogs : ",bg="#D9EEE1", fg='#282A35',font=('Verdana', 12,"bold"))
    lb12.place(relx=0.14, rely=0.65, relheight=0.04)
    defaultBacklog = StringVar()
    defaultBacklog.set("Select No. Of Backlogs")
    backlogs = [0,1,2,3]
    stdInfo12 = OptionMenu(root,defaultBacklog,*backlogs)
    stdInfo12.pack()
    stdInfo12.place(relx=0.28, rely=0.65, relwidth=0.22, relheight=0.04)

    # average cgpa
    lb13 = Label(root, text="Avg CGPA : ",bg="#D9EEE1", fg='#282A35',font=('Verdana', 12,"bold"))
    lb13.place(relx=0.5, rely=0.65, relheight=0.04)

    stdInfo13 = Entry(root)
    stdInfo13.place(relx=0.64, rely=0.65, relwidth=0.23, relheight=0.04)

    #import data from csv
    ImportBtn = Button(root, text="Or Import Data from csv file.", bg='#FFF4A3', fg='#282A35', command=importData,font=('Verdana', 12))
    ImportBtn.place(relx=0.14, rely=0.75, relwidth=0.73, relheight=0.04)


    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#059862', fg='#ffffff', command=studentRegister,font=('Verdana', 12))
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#059862', fg='#ffffff', command=root.destroy,font=('Verdana', 12))
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

addStudents()

