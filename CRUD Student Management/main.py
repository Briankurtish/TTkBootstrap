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

# style


# Buttons

add_btn = tb.Button(root, text="Add", width=20, style="success outline")
add_btn.grid(row=3, column=5, columnspan=1, rowspan=2, padx=90, pady=25)

update_btn = tb.Button(root, text="Update", width=20, bootstyle="info outline")
update_btn.grid(row=4, column=5, columnspan=1, rowspan=2)

delete_btn = tb.Button(root, text="Delete", width=20,
                       bootstyle="danger outline")
delete_btn.grid(row=5, column=5, columnspan=1, rowspan=2, padx=90, pady=25)

search_btn = tb.Button(root, text="Search", width=20,
                       bootstyle="primary outline")
search_btn.grid(row=6, column=5, columnspan=1, rowspan=2, padx=90, pady=25)

reset_btn = tb.Button(root, text="Reset", width=20,
                      bootstyle="warning outline")
reset_btn.grid(row=7, column=5, columnspan=1, rowspan=2, padx=90, pady=25)

select_btn = tb.Button(root, text="Select", width=20,
                       bootstyle="secondary outline")
select_btn.grid(row=8, column=5, columnspan=1, rowspan=2, padx=90, pady=25)

root.mainloop()
