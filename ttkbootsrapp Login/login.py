from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="cyborg")
root.title("Login")
root.geometry('900x700')


# Create Top Label

title = tb.Label(root, text="Welcome Cipher!", font=(
    "Heveltica", 25), bootstyle="light")
title.pack(pady=20)

root.mainloop()
