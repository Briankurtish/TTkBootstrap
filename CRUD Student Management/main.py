import pymysql
from tkinter import *
import ttkbootstrap as tb
from tkinter import ttk
from tkinter import messagebox


# connection to database
def connection():
    conn = pymysql.connect(
        host='localhost', user='root', password='', db='student_db'
    )
    return conn


def refreshTable():
    for data in record_table.get_children():
        record_table.delete(data)

    for array in read():
        record_table.insert(parent='', index='end', iid=array,
                            text="", values=(array), tag="orow")
        record_table.tag_configure(
            'orow', background='#EEEEEE', font=("Arial", 12))
        record_table.grid(row=8, column=0, columnspan=4,
                          rowspan=11, padx=10, pady=20)


# GUI
root = tb.Window(themename="lumen")
root.title("Student Registeration System")
root.geometry("1200x720")


# Placeholders for entry
ph1 = StringVar()
ph2 = StringVar()
ph3 = StringVar()
ph4 = StringVar()
ph5 = StringVar()

# set placeholder values


def setph(word, num):
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)
    if num == 5:
        ph5.set(word)


# Functions


def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def add():
    studid = str(studidEntry.get())
    fname = str(fnameEntry.get())
    lname = str(lnameEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())

    if (studid == "" or studid == " ") or (fname == "" or fname == " ") or (lname == "" or lname == " ") or (address == "" or address == " ") or (phone == "" or phone == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students VALUES ('"+studid +
                           "','"+fname+"','"+lname+"','"+address+"','"+phone+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()


# This functions deletes everything from the database


def reset():
    decision = messagebox.askquestion("Warning!", "Delete all Data?")
    if decision != 'yes':
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

    refreshTable()


# This functions deletes everything from the database


def delete():
    decision = messagebox.askquestion("Warning!", "Delete the selected data?")
    if decision != 'yes':
        return
    else:
        selected_item = record_table.selection()[0]
        deleteData = str(record_table.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM students WHERE STUDID='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

    refreshTable()


def select():

    try:
        selected_item = record_table.selection()[0]
        studid = str(record_table.item(selected_item)['values'][0])
        fname = str(record_table.item(selected_item)['values'][1])
        lname = str(record_table.item(selected_item)['values'][2])
        address = str(record_table.item(selected_item)['values'][3])
        phone = str(record_table.item(selected_item)['values'][4])

        setph(studid, 1)
        setph(fname, 2)
        setph(lname, 3)
        setph(address, 4)
        setph(phone, 5)

    except:
        messagebox.showinfo("Error", "Please Select a Data Row")


def search():
    studid = str(studidEntry.get())
    fname = str(fnameEntry.get())
    lname = str(lnameEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE STUDID= '" +
                   studid+"' or FNAME='" + fname+"' or LNAME= '" + lname+"' or ADDRESS= '" + address+"' or PHONE='" + phone + "'")
    try:
        results = cursor.fetchall()
        for num in range(0, 5):
            setph(results[0][num], (num+1))
        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No Data Found")


def update():
    selectedStudid = ""

    try:
        selected_item = record_table.selection()[0]
        selectedStudid = str(record_table.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    studid = str(studidEntry.get())
    fname = str(fnameEntry.get())
    lname = str(lnameEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())

    if (studid == "" or studid == " ") or (fname == "" or fname == " ") or (lname == "" or lname == " ") or (address == "" or address == " ") or (phone == "" or phone == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET STUDID='" +
                           studid+"', FNAME='" +
                           fname+"', LNAME='" +
                           lname+"', ADDRESS='" +
                           address+"', PHONE='" +
                           phone+"' WHERE STUDID='" +
                           selectedStudid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()


# Labels
label = tb.Label(root, text="Student Registration System",
                 font=("Arial Bold", 30), bootstyle='primary')
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

studidLabel = tb.Label(root, text="Stud ID", font=("Arial", 15))
studidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)

fnameLabel = tb.Label(root, text="First Name", font=("Arial", 15))
fnameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)

lnameLabel = tb.Label(root, text="Last Name", font=("Arial", 15))
lnameLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)

addressLabel = tb.Label(root, text="Address", font=("Arial", 15))
addressLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)

phoneLabel = tb.Label(root, text="Phone", font=("Arial", 15))
phoneLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)


# entries
studidEntry = tb.Entry(root, width=55, bootstyle='info', textvariable=ph1)
studidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)

fnameEntry = tb.Entry(root, width=55, bootstyle='info', textvariable=ph2)
fnameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)

lnameEntry = tb.Entry(root, width=55, bootstyle='info', textvariable=ph3)
lnameEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)

addressEntry = tb.Entry(root, width=55, bootstyle='info', textvariable=ph4)
addressEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)

phoneEntry = tb.Entry(root, width=55, bootstyle='info', textvariable=ph5)
phoneEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

# style
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial Bold", 14))
style.configure("Treeview", background="silver",
                foreground="black", fieldbackground="green")

style.map("Treeview", background=[('selected', 'green')])

# Buttons

add_btn = tb.Button(root, text="Add", width=20,
                    style="success", command=add)
add_btn.grid(row=3, column=5, columnspan=1, rowspan=2, padx=90, pady=25)

update_btn = tb.Button(root, text="Update", width=20,
                       bootstyle="info", command=update)
update_btn.grid(row=4, column=5, columnspan=1, rowspan=2)

delete_btn = tb.Button(root, text="Delete", width=20,
                       bootstyle="danger", command=delete)
delete_btn.grid(row=5, column=5, columnspan=1, rowspan=2, padx=90, pady=25)

search_btn = tb.Button(root, text="Search", width=20,
                       bootstyle="primary", command=search)
search_btn.grid(row=6, column=5, columnspan=1, rowspan=2, padx=90, pady=25)

reset_btn = tb.Button(root, text="Reset", width=20,
                      bootstyle="warning", command=reset)
reset_btn.grid(row=7, column=5, columnspan=1, rowspan=2, padx=90, pady=25)

select_btn = tb.Button(root, text="Select", width=20,
                       bootstyle="secondary", command=select)
select_btn.grid(row=8, column=5, columnspan=1, rowspan=2, padx=90, pady=25)


record_table = ttk.Treeview(root, bootstyle="primary")


record_table["column"] = ['Stud ID',
                          "FirstName", "LastName", "Address", "Phone"]
record_table.column('#0', width=0, stretch=NO)
record_table.column("Stud ID", anchor=W, width=170)
record_table.column("FirstName", anchor=W, width=150)
record_table.column("LastName", anchor=W, width=150)
record_table.column("Address", anchor=W, width=165)
record_table.column("Phone", anchor=W, width=170)

record_table.heading("Stud ID", text="Student ID", anchor=W)
record_table.heading("FirstName", text="FirstName", anchor=W)
record_table.heading("LastName", text="LastName", anchor=W)
record_table.heading("Address", text="Adress", anchor=W)
record_table.heading("Phone", text="Phone", anchor=W)


refreshTable()

root.mainloop()
