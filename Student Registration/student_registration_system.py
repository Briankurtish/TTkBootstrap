from tkinter import *
import tkinter.ttk as ttk
import ttkbootstrap as tb


root = tb.Window(themename="superhero")
root.title("Student registration System")
root.geometry("500x600")

student_data = []


def load_student_data():
    for item in record_table.get_children():
        record_table.delete(item)

        for r in range(len(student_data)):
            record_table.insert(parent='', index='end',
                                text='', iid=r, values=student_data[r])


def add_student_data(stud_id, stud_name, stud_email, stud_courses):
    student_data.append([stud_id, stud_name, stud_email, stud_courses])

    load_student_data()


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
student_id.place(x=130, y=50, width=180)

# Student Name
student_name_lb = tb.Label(
    head_frame, text="Student Name: ", font=("Bold", 10))
student_name_lb.place(x=0, y=100)

# Student Name entry
student_name = tb.Entry(head_frame, font=("Bold", 10), bootstyle="info")
student_name.place(x=130, y=100, width=180)


# Student Email
student_email_lb = tb.Label(
    head_frame, text="Student Email: ", font=("Bold", 10))
student_email_lb.place(x=0, y=150)

# Student Email entry
student_email = tb.Entry(head_frame, font=("Bold", 10), bootstyle="info")
student_email.place(x=130, y=150, width=180)


# Student Courses
student_courses_lb = tb.Label(
    head_frame, text="Student courses: ", font=("Bold", 10))
student_courses_lb.place(x=0, y=200)

# Student Courses entry
student_courses = tb.Entry(head_frame, font=("Bold", 10), bootstyle="info")
student_courses.place(x=130, y=200, width=180)

# Register Button
register_btn = tb.Button(head_frame, text='Register',
                         bootstyle="success outline", command=lambda:
                             add_student_data(student_id.get(),
                                              student_name.get(),
                                              student_email.get(),
                                              student_courses.get()))
register_btn.place(x=0, y=250)

# Update Button
register_btn = tb.Button(head_frame, text='Update',
                         bootstyle="primary outline")
register_btn.place(x=100, y=250)

# Delete Button
delete_btn = tb.Button(head_frame, text='Delete',
                       bootstyle="danger outline")
delete_btn.place(x=200, y=250)

# Clear Button
clear_btn = tb.Button(head_frame, text='Clear',
                      bootstyle="info outline")
clear_btn.place(x=300, y=250)


head_frame.pack(pady=10)
# When you use pack_propagate you can resize the Frame like a container and give it a width and height
head_frame.pack_propagate(False)
head_frame.config(width=400, height=300)


# Search Bar Frame
search_bar_frame = tb.Frame(root)
# saecrh bar Label
search_lb = tb.Label(
    search_bar_frame, text='Search Student By Id:', font=("Bold", 10))
search_lb.pack(anchor=tb.W)

# Search Bar Entry
search_entry = tb.Entry(search_bar_frame, font=("Bold", 10), bootstyle="info")
search_entry.pack(anchor=tb.W)

search_bar_frame.pack(pady=0)
search_bar_frame.pack_propagate(False)
search_bar_frame.configure(width=400, height=50)


record_frame = tb.Frame(root)

record_lb = tb.Label(record_frame, text="Select Record or Delete or Update",
                     bootstyle="warning", font=("Bold", 13))
record_lb.pack(fill=tb.X)

record_table = tb.Treeview(record_frame, bootstyle="success")
record_table.pack(fill=tb.X, pady=5)

record_table["column"] = ['Id', "Name", "Email", "Courses"]
record_table.column('#0', anchor=tb.W, width=0, stretch=tb.NO)

record_table.column('Id', anchor=tb.W, width=50)
record_table.column('Name', anchor=tb.W, width=100)
record_table.column('Email', anchor=tb.W, width=120)
record_table.column('Courses', anchor=tb.W, width=160)

record_table.heading("Id", text="Id", anchor=tb.W)
record_table.heading("Name", text="Name", anchor=tb.W)
record_table.heading("Email", text="Email", anchor=tb.W)
record_table.heading("Courses", text="Courses", anchor=tb.W)


record_frame.pack(pady=10)
record_frame.pack_propagate(False)
record_frame.configure(width=400, height=200)


root.mainloop()
