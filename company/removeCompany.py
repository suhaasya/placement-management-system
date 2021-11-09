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

## Add your own database name and password here to reflect in the code
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

#List To store all company IDs
allCid = []

def remove():
    global removeBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    cid = inf1.get()

    selectStatement = f'SELECT * from {companiesTable} WHERE company_id={cid};'
    try:
        cur.execute(selectStatement)
        for i in cur:
            allCid.append(i[0])

        if cid not in allCid:
            messagebox.showinfo("Error", "Company ID not present")
            return
    except:
        messagebox.showinfo("Error", "Can't fetch Company IDs")

    deleteStatement = f'DELETE FROM {companiesTable} WHERE company_id={cid};'
    try:
        cur.execute(deleteStatement)
        con.commit()
        messagebox.showinfo('Success', "Company removed")
        root.destroy()
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")


def removeCompany():
    global stdInfo1, stdInfo2, stdInfo3, stdInfo4, Canvas1, con, cur, stdTable, root, inf1

    root = Tk()
    root.title("PM Tool")
    root.geometry("1080x720")



    Canvas1 = Canvas(root)

    Canvas1.config(bg="#FFF4A3")
    Canvas1.pack(expand=True, fill=BOTH)

    headingLabel = Label(root, text="Remove Company Details", bg='#FFF4A3', fg='#000000',
                         font=('Verdana', 40, 'bold'))
    headingLabel.place(relx=0.08, rely=0.1)

    # student ID
    lb1 = Label(root, text="Enter CID : ", bg="#FFF4A3", fg='#282A35', font=('Verdana', 12, "bold"))
    lb1.place(relx=0.12, rely=0.3, relheight=0.04)

    inf1 = Entry(root)
    inf1.place(relx=0.25, rely=0.3, relwidth=0.62, relheight=0.04)



    # Submit Button
    SubmitBtn = Button(root, text="Remove Company", bg='#059862', fg='#ffffff', command=remove, font=('Verdana', 12))
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#059862', fg='#ffffff', command=root.destroy, font=('Verdana', 12))
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
# removeCompany()