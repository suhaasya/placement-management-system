from tkinter import *
from  tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

from student.AddStudent import *
from student.eligibleCompany import *
from student.removeStudent import *
from student.ViewStudents import *
import os
import sys
sys.path.append(f'{os.getcwd()}')
from configurations import config

def student():
    root = Tk()
    root.title("PM Tool")
    root.minsize(width=500, height=500)
    root.geometry("1080x720")

    



    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D9EEE1")
    Canvas1.pack(expand=True, fill=BOTH)

    headingLabel = Label(root, text="Student Section", bg='#D9EEE1', fg='#000000',
                         font=('Verdana', 40, 'bold'))
    headingLabel.place(relx=0.23, rely=0.1)

    btn1 = Button(root, text="Add Student Details", bg='#282A35', fg='white', command=addStudents, font=('Verdana', 12))
    btn1.place(relx=0.28, rely=0.35, relwidth=0.45, relheight=0.08)

    btn2 = Button(root, text="Delete Student Details", bg='#282A35', fg='white', command=removeStudent, font=('Verdana', 12))
    btn2.place(relx=0.28, rely=0.45, relwidth=0.45, relheight=0.08)

    btn3 = Button(root, text="View Student Details", bg='#282A35', fg='white', command=ViewStudent, font=('Verdana', 12))
    btn3.place(relx=0.28, rely=0.55, relwidth=0.45, relheight=0.08)

    btn4 = Button(root, text="View Eligibile Companies", bg='#282A35', fg='white', command=ViewEligibleCompany, font=('Verdana', 12))
    btn4.place(relx=0.28, rely=0.65, relwidth=0.45, relheight=0.08)

    btn5 = Button(root, text="Back", bg='#059862', fg='#ffffff', command=root.destroy, font=('Verdana', 12))
    btn5.place(relx=0.38, rely=0.85, relwidth=0.225, relheight=0.1)



    root.mainloop()

# student()