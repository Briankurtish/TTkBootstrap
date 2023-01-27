from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="superhero")
root.title("Button Size")
root.geometry("500x350")

# Style
my_style = tb.Style()
my_style.configure('success.TButton', font=("Helvetica", 18))

my_button = tb.Button(text="Hello World",
                      bootstyle="success", style='success.TButton', width=60)
my_button.pack(pady=20)

root.mainloop()
