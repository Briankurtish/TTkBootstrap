from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

root.title("ComboBox")
root.geometry("500x350")

my_label = tb.Label(root, text="Hello World", font=('Helvetica', 18))
my_label.pack(pady=30)


root.mainloop()
