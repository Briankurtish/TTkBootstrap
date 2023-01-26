from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

root.title("ComboBox")
root.geometry("500x350")


def clicker():
    my_label.config(text=f"You clicked {my_combo.get()}!")

# Create Binding Function


def click_bind(e):
    my_label.config(text=f"You clicked {my_combo.get()}!")


my_label = tb.Label(root, text="Hello World", font=('Helvetica', 18))
my_label.pack(pady=30)

# Create DropDown Options
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create Combobox
my_combo = tb.Combobox(root, bootstyle="success", values=days)
my_combo.pack(pady=20)

# set combo default
my_combo.current(0)

# Create a Button
my_button = tb.Button(root, text="Click Me!",
                      command=clicker, bootstyle="danger")
my_button.pack(pady=20)

# Bind the combobox
my_combo.bind("<<ComboboxSelected>>", click_bind)

root.mainloop()
