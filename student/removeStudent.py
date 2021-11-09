from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import os
import sys
sys.path.append(f'{os.getcwd()}')
from configurations import config
import ctypes

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

#List To store all company IDs
allPrn = []

def remove():
    global removeBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    prn = inf1.get()
    print(prn)

    selectStatement = f'SELECT * from {studentTable} WHERE PRN="{prn}";'
    print(selectStatement)
    try:
        cur.execute(selectStatement)
        for i in cur:
            # print(i)
            allPrn.append(i[0])
        print(allPrn)

        if prn not in allPrn:
            # print(prn)
            messagebox.showinfo("Error", "Student with this ID not present")
            return
    except:
        messagebox.showinfo("Error", "Can't fetch Company IDs")

    deleteStatement = f'DELETE FROM {studentTable} WHERE PRN="{prn}";'
    try:
        cur.execute(deleteStatement)
        con.commit()
        messagebox.showinfo('Success', "Student removed")
        root.destroy()
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")


def removeStudent():
    global stdInfo1, stdInfo2, stdInfo3, stdInfo4, Canvas1, con, cur, stdTable, root, inf1

    root = Tk()
    root.title("PM Tool")
    root.geometry("1080x720")



    Canvas1 = Canvas(root)

    Canvas1.config(bg="#D9EEE1")
    Canvas1.pack(expand=True, fill=BOTH)

    headingLabel = Label(root, text="Remove Student Details", bg='#D9EEE1', fg='#000000',
                         font=('Verdana', 40, 'bold'))
    headingLabel.place(relx=0.08, rely=0.1)

    # student ID
    lb1 = Label(root, text="Enter PRN : ", bg="#D9EEE1", fg='#282A35', font=('Verdana', 12, "bold"))
    lb1.place(relx=0.12, rely=0.3, relheight=0.04)

    inf1 = Entry(root)
    inf1.place(relx=0.25, rely=0.3, relwidth=0.62, relheight=0.04)



    # Submit Button
    SubmitBtn = Button(root, text="Remove Student", bg='#059862', fg='#ffffff', command=remove, font=('Verdana', 12))
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#059862', fg='#ffffff', command=root.destroy, font=('Verdana', 12))
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
# removeStudent()