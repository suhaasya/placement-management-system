from tkinter import *
from  tkinter import ttk
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox

from company.ViewCompany import *
from company.eligibleStudents import *
from company.addCompany import *
from company.removeCompany import *
import os
import sys
sys.path.append(f'{os.getcwd()}')
from configurations import config

def company():
    root = Tk()
    root.title("PM Tool")
    root.geometry("1080x720")

    



    Canvas1 = Canvas(root)
    Canvas1.config(bg="#FFF4A3")
    Canvas1.pack(expand=True, fill=BOTH)

    headingLabel = Label(root, text="Company Section", bg='#FFF4A3', fg='#000000',
                         font=('Verdana', 40, 'bold'))
    headingLabel.place(relx=0.23, rely=0.1)

    btn1 = Button(root, text="Add Company Details", bg='#282A35', fg='white', command=addCompany, font=('Verdana', 12))
    btn1.place(relx=0.28, rely=0.35, relwidth=0.45, relheight=0.08)

    btn2 = Button(root, text="Delete Company Details", bg='#282A35', fg='white', command=removeCompany, font=('Verdana', 12))
    btn2.place(relx=0.28, rely=0.45, relwidth=0.45, relheight=0.08)

    btn3 = Button(root, text="View Company Details", bg='#282A35', fg='white', command=ViewCompany, font=('Verdana', 12))
    btn3.place(relx=0.28, rely=0.55, relwidth=0.45, relheight=0.08)

    btn4 = Button(root, text="View Eligibile Students", bg='#282A35', fg='white', command=ViewEligibleStudent, font=('Verdana', 12))
    btn4.place(relx=0.28, rely=0.65, relwidth=0.45, relheight=0.08)

    btn5 = Button(root, text="Back", bg='#059862', fg='#ffffff', command=root.destroy, font=('Verdana', 12))
    btn5.place(relx=0.38, rely=0.85, relwidth=0.225, relheight=0.1)



    root.mainloop()

# company()