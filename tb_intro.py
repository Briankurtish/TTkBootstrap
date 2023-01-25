from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb


root = tb.Window(themename="superhero")
root.title("TTk Bootstrap")
root.geometry('500x350')


# Creating a Label
my_label = tb.Label(text="Hello World", font=(
    "Helvetica", 28), bootstyle="danger")
my_label.pack(pady=50)

my_button = tb.Button()

root.mainloop()
