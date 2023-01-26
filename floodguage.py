from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("Floodguage")
root.geometry("500x350")

# Create Floodgauge

my_gauue = tb.Floodgauge(root, bootstyle="success",
                         font=("Helvetica", 18), mask="Pos: {}%", maximum=100, orient="horizontal", value=10)
my_gauue.pack(pady=50, fill=X, padx=20)


root.mainloop()
