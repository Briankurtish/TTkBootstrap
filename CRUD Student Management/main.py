import pymysql
from tkinter import *
import ttkbootstrap as tb
from tkinter import ttk
from tkinter import messagebox


# connection to database


# GUI

root = tb.Window(themename="darkly")
root.title("Student Registeration System")
root.geometry("1080x720")
mt_tree = ttk.Treeview(root)

# Functions

# Gui
label = tb.Label(root, text="Student Registration System",
                 font=("Arial Bold", 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)


root.mainloop()
