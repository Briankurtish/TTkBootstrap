from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("Entry Widget")
root.geometry("500x350")

# Create Entry function


# Create Entry Widget
my_entry = tb.Entry(root)
my_entry.pack(pady=20)

# Create Button
my_button = tb.Button(root, text="Click Me!",
                      bootstyle="danger outline", command=())
my_button.pack(pady=20)

# Create Label


root.mainloop()
