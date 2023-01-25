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


# ToolButton

var2 = IntVar()

my_check2 = tb.Checkbutton(text="ToolButton!", bootstyle=(
    "danger, toolbutton"), variable=var2, offvalue=0, onvalue=1, command=checker)
my_check2.pack(pady=10)

# Outline ToolButton

var3 = IntVar()

my_check3 = tb.Checkbutton(text="ToolButton!", bootstyle=(
    "success, toolbutton, outline"), variable=var3, offvalue=0, onvalue=1, command=checker)
my_check3.pack(pady=10)

# Round Toggle Button

var4 = IntVar()

my_check4 = tb.Checkbutton(text="Round Toggle Button", bootstyle=(
    "info, round-toggle"), variable=var4, offvalue=0, onvalue=1, command=checker)
my_check4.pack(pady=10)

root.mainloop()
