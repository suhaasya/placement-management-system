from tkinter import *
from  tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import os
import sys
sys.path.append(f'{os.getcwd()}')
from configurations import config
import ctypes





# quality
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def ViewCompany():
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
    Email VARCHAR(255)
    )""");

    ws  = Tk()
    ws.title('ViewCompany')
    ws.geometry('1080x720')
    ws['bg'] = '#FFF4A3'

    

    headingLabel = Label(ws, text="Company Details", bg='#FFF4A3', fg='#000000',
                         font=('Verdana', 40, 'bold'))
    headingLabel.place(relx=0.2, rely=0.1)

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




    viewC['columns'] = ('CID', 'Name', 'Required_CGPA', 'Email','Phone_No')

    viewC.column("#0", width=0,  stretch=NO)
    viewC.column("CID",anchor=W, width=220)
    viewC.column("Name",anchor=W,width=220)
    viewC.column("Required_CGPA",anchor=W,width=220)
    viewC.column("Email",anchor=W,width=220)
    viewC.column("Phone_No",anchor=W,width=220)


    viewC.heading("#0",text="",anchor=W)
    viewC.heading("CID",text="Company ID",anchor=W)
    viewC.heading("Name",text="Company Name",anchor=W)
    viewC.heading("Required_CGPA",text="Required_CGPA",anchor=W)
    viewC.heading("Email",text="Email",anchor=W)
    viewC.heading("Phone_No",text="Phone_No",anchor=W)

    getCompany = "select * from " + companiesTable
    try:
        cur.execute(getCompany)
        for i in cur:
            # print(i)
            viewC.insert(parent='', index='end', iid=i, text='',values=(i[0],i[1],i[2],i[3],i[4]))
    except:
        messagebox.showinfo("Failed to fetch files from database")



    viewC.pack()

    quitBtn = Button(ws, text="Quit", bg='#059862', fg='#ffffff', command=ws.destroy, font=('Verdana', 12))
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    ws.mainloop()

# ViewCompany()
