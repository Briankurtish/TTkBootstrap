from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="superhero")
root.title("Student registration System")
root.geometry("500x600")

head_frame = tb.Frame(root)

# Heading label
heading_lb = tb.Label(head_frame, text="Student Registration System", font=(
    "Bold", 13), bootstyle="danger")
heading_lb.pack(pady=5)

# Student Id label
student_id_lb = tb.Label(head_frame, text="Student Id: ", font=("Bold", 10))
student_id_lb.place(x=0, y=50)

head_frame.pack(pady=10)
# When you use pack_propagate you can resize the Frame like a container and give it a width and height
head_frame.pack_propagate(False)
head_frame.config(width=400, height=300)


root.mainloop()
