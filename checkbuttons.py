from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb


root = tb.Window(themename="solar")
root.title("TTk Bootsrtap CheckButtons")
root.geometry("500x350")


my_label = tb.Label(text="Click the checkbutton below", font={"Helvetica, 18"})
my_label.pack(pady=(40, 10))


root.mainloop()
