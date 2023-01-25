from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb


root = tb.Window(themename="solar")
root.title("TTk Bootsrtap CheckButtons")
root.geometry("500x350")


def checker():
    if var1.get() == 1:
        my_label.config(text="Checked!")
    else:
        my_label.config(text="Unchecked!")


my_label = tb.Label(text="Click the checkbutton below", font={"Helvetica, 18"})
my_label.pack(pady=(40, 10))

# Checkbutton

var1 = IntVar()
my_check = tb.Checkbutton(
    bootstyle="info", text="Check Me Out!", variable=var1, onvalue=1, offvalue=0, command=checker)
my_check.pack(pady=10)


root.mainloop()
