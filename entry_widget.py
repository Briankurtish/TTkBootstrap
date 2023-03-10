from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("Entry Widget")
root.geometry("500x350")

# Create Entry function


def speak():
    my_label.config(text=f"You typed: {my_entry.get()}")


# Create Entry Widget
my_entry = tb.Entry(root, bootstyle="warning", font=(
    "Helevtica", 18), foreground="blue", show="*")
my_entry.pack(pady=20)

# Create Button
my_button = tb.Button(root, text="Click Me!",
                      bootstyle="danger outline", command=speak)
my_button.pack(pady=20)

# Create Label
my_label = tb.Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
