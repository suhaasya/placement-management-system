from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ctypes
import mysql.connector
import ctypes
import csv
from tkinter import *
from tkinter import filedialog
import os
import sys
sys.path.append(f'{os.getcwd()}')
from configurations import config

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


def importData():
    rows = []
    def openFile():
        filepath = filedialog.askopenfilename()
        file = open(filepath)
        csvreader = csv.reader(file)
        err = False;
        for row in csvreader:
            rows.append(row)

            insertCompany = f"insert into {companiesTable} values({row[0]},'{row[1]}',{(row[2])},'{row[3]}',{row[4]})"
            # insertCompany = "insert into " + companiesTable + " values('" + row[0] + "','" + row[1] + "','" + row[2] + "','" + row[3] + "','" + row[4] + "')"
            try:
                print(insertCompany)
                cur.execute(insertCompany)
                con.commit()
                
            except:
                err = True
                messagebox.showinfo("Error", "Can't add data into Database Data Already Added")
                break

        print(rows)
        if(not err):
            print(err)
            messagebox.showinfo('Success', "Student details added successfully")
        
        file.close()
        window.destroy()
        
        

    window = Tk()
    button = Button(window, text="select csv file", command=openFile)
    button.pack(padx=100,pady=10)
    window.mainloop()

def bookRegister():
    company_id = compInfo1.get()
    company_name = compInfo2.get()
    required_cgpa = compInfo3.get()
    Email = compInfo4.get()
    Email = Email.lower()
    phone_no = compInfo5.get()

    insertCompany = "insert into " + companiesTable + " values('" + company_id + "','" + company_name + "','" + required_cgpa + "','" + Email + "','" + phone_no + "')"
    try:
        cur.execute(insertCompany)
        con.commit()
        messagebox.showinfo('Success', "Company details added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")





    root.destroy()


def addCompany():
    global compInfo1, compInfo2, compInfo3, compInfo4,compInfo5, Canvas1, con, cur, companiesTable, root

    root = Tk()
    root.title("PM Tool")
    root.geometry("1080x720")

    


    Canvas1 = Canvas(root)

    Canvas1.config(bg="#FFF4A3")
    Canvas1.pack(expand=True, fill=BOTH)

    headingLabel = Label(root, text="Add Company Details", bg='#FFF4A3', fg='#000000',
                         font=('Verdana', 40, 'bold'))
    headingLabel.place(relx=0.18, rely=0.1)

    # student ID
    lb1 = Label(root, text="CID : ",bg="#FFF4A3", fg='#282A35',font=('Verdana', 12,"bold"))
    lb1.place(relx=0.1, rely=0.3, relheight=0.04)

    compInfo1 = Entry(root)
    compInfo1.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.04)

    # name
    lb2 = Label(root, text="Name : ",bg="#FFF4A3", fg='#282A35',font=('Verdana', 12,"bold"))
    lb2.place(relx=0.1, rely=0.35, relheight=0.04)

    compInfo2 = Entry(root)
    compInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.04)

    # department
    lb3 = Label(root, text="Required_Score : ",bg="#FFF4A3", fg='#282A35',font=('Verdana', 12,"bold"))
    lb3.place(relx=0.1, rely=0.40, relheight=0.04)

    compInfo3 = Entry(root)
    compInfo3.place(relx=0.3, rely=0.40, relwidth=0.62, relheight=0.04)

    # email
    lb4 = Label(root, text="Email : ",bg="#FFF4A3", fg='#282A35',font=('Verdana', 12,"bold"))
    lb4.place(relx=0.1, rely=0.45, relheight=0.04)

    compInfo4 = Entry(root)
    compInfo4.place(relx=0.3, rely=0.45, relwidth=0.62, relheight=0.04)

    # phone no
    lb5 = Label(root, text="Phone No. : ",bg="#FFF4A3", fg='#282A35',font=('Verdana', 12,"bold"))
    lb5.place(relx=0.1, rely=0.50, relheight=0.04)

    compInfo5 = Entry(root)
    compInfo5.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.04)

    #import data
    #import data from csv
    ImportBtn = Button(root, text="Or Import Data from csv file.", bg='#D9EEE1', fg='#282A35', command=importData,font=('Verdana', 12))
    ImportBtn.place(relx=0.14, rely=0.75, relwidth=0.73, relheight=0.04)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#059862', fg='#ffffff', command=bookRegister,font=('Verdana', 12))
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#059862', fg='#ffffff', command=root.destroy,font=('Verdana', 12))
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

# addCompany()