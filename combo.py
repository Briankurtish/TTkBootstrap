from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

root.title("ComboBox")
root.geometry("500x350")

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

root.mainloop()
