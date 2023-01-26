from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="cyborg")
root.title("Login")
root.geometry('700x700')


# Style
my_style = tb.Style()
my_style.configure('primary-outline.TButton', font=("Helvetica", 14))

# Create Top Label

title = tb.Label(root, text="Welcome Cipher!", font=(
    "Heveltica", 25), bootstyle="light")
title.grid(row=0, column=3, pady=30)

label2 = tb.Label(
    root, text="Fill the information below to login", font=("Heveltica", 9))
label2.grid(row=1, column=3)

# Create email entry widgets
email_label = tb.Label(
    root, text="Enter Email:", font=("Heveltica", 9))
email_label.grid(row=2, column=2, padx=50)
email_entry = tb.Entry(root, bootstyle="success")
email_entry.grid(row=2, column=3, pady=30)

# Create Password entry widgets
password_label = tb.Label(
    root, text="Enter Password:", font=("Heveltica", 9))
password_label.grid(row=3, column=2, padx=50)
password_entry = tb.Entry(root, bootstyle="success", show="*")
password_entry.grid(row=3, column=3, pady=30)


# Create login Button

login_btn = tb.Button(
    text="Login Now!", style='primary.TButton')
login_btn.grid(row=4, column=3)


root.mainloop()
