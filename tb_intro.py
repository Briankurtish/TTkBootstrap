from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

counter = 0


def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        my_label.config(text="Hello World")
    else:
        my_label.config(text="Goodbye World")


root = tb.Window(themename="superhero")
root.title("TTk Bootstrap")
root.geometry('500x350')


# Creating a Label
my_label = tb.Label(text="Hello World", font=(
    "Helvetica", 28), bootstyle="danger")
my_label.pack(pady=50)

my_button = tb.Button(
    text="Click Me!", bootstyle="success, outline", command=changer)
my_button.pack(pady=20)

root.mainloop()
