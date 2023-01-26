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

# Student Id Entry
student_id = tb.Entry(head_frame, font=("Bold", 10), bootstyle="info")
student_id.place(x=120, y=50, width=180)

# Student Name
student_name_lb = tb.Label(
    head_frame, text="Student Name: ", font=("Bold", 10))
student_name_lb.place(x=0, y=100)

# Student Name entry
student_name = tb.Entry(head_frame, font=("Bold", 10), bootstyle="info")
student_name.place(x=120, y=100, width=180)


# Student Email
student_email_lb = tb.Label(
    head_frame, text="Student Email: ", font=("Bold", 10))
student_email_lb.place(x=0, y=150)

# Student Email entry
student_email = tb.Entry(head_frame, font=("Bold", 10), bootstyle="info")
student_email.place(x=120, y=150, width=180)


head_frame.pack(pady=10)
# When you use pack_propagate you can resize the Frame like a container and give it a width and height
head_frame.pack_propagate(False)
head_frame.config(width=400, height=300)


root.mainloop()
