from tkinter import *
from  tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import ctypes


from student.studentMain import *
from company.CompanyMain import *
from test import *



ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("Home")
root.minsize(width=500, height=500)
root.geometry("1080x720")


# Adding a background

Canvas1 = Canvas(root)
Canvas1.config(bg="#282A35")
Canvas1.pack(expand=True, fill=BOTH)


headingLabel = Label(root, text="Welcome to \n Placement Cell", bg='#282A35', fg='#ffffff', font=('Verdana', 30, 'bold'))
headingLabel.place(relx=0.30, rely=0.1)

btn1 = Button(root, text="Student section", bg='#059862', fg='#ffffff', command=student, font=('Verdana', 12))
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Company section", bg='#059862', fg='#ffffff', command=company, font=('Verdana', 12))
btn2.place(relx=0.28, rely=0.52, relwidth=0.45, relheight=0.1)



root.mainloop()
