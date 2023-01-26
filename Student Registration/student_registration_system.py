from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="superhero")
root.title("Student registration System")
root.geometry("500x600")

head_frame = tb.Frame(root)
head_frame.pack(pady=10)
# When you use pack_propagate you can resize the Frame like a container and give it a width and height
head_frame.pack_propagate(False)
head_frame.config(width=500, height=600)


root.mainloop()
