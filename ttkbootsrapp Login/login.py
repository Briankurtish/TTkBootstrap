from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="cyborg")
root.title("Login")
root.geometry('700x700')


# Create Top Label

title = tb.Label(root, text="Welcome Cipher!", font=(
    "Heveltica", 25), bootstyle="light")
title.grid(row=0, column=3, pady=30)

label2 = tb.Label(
    root, text="Fill the information below to login", font=("Heveltica", 9))
label2.grid(row=1, column=3)

# Create email entry widgets
label3 = tb.Label(
    root, text="Enter Email:", font=("Heveltica", 9))
label3.grid(row=2, column=2, padx=50)
email_entry = tb.Entry(root, bootstyle="success", textvariable="Enter Email")
email_entry.grid(row=2, column=3, pady=30)


root.mainloop()
