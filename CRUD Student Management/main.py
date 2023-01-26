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

# Labels
label = tb.Label(root, text="Student Registration System",
                 font=("Arial Bold", 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

studidLabel = tb.Label(root, text="Stud ID", font=("Arial", 15))
studidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)

fnameLabel = tb.Label(root, text="First Name", font=("Arial", 15))
fnameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)

lnameLabel = tb.Label(root, text="Last Name", font=("Arial", 15))
lnameLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)

addressLabel = tb.Label(root, text="Address", font=("Arial", 15))
addressLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)

phoneLabel = tb.Label(root, text="Phone", font=("Arial", 15))
phoneLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)


# entries
studidEntry = tb.Entry(root, width=55)
studidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)

fnameEntry = tb.Entry(root, width=55)
fnameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)

lnameEntry = tb.Entry(root, width=55)
lnameEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)

addressEntry = tb.Entry(root, width=55)
addressEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)

phoneEntry = tb.Entry(root, width=55)
phoneEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)


root.mainloop()
