from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("Floodguage")
root.geometry("500x550")


def starter():
    # Start the Gauue
    my_gauue.start()


def stopper():
    # Stop the Gauge
    my_gauue.stop()


def increment():
    # Increment Guaue
    my_gauue.step(10)
    my_label.config(text=f"Position: {my_gauue.variable.get()}")


# Create Floodgauge
my_gauue = tb.Floodgauge(root, bootstyle="success",
                         font=("Helvetica", 18), mask="Pos: {}%", maximum=100, orient="horizontal", value=0, mode="determinate")
my_gauue.pack(pady=50, fill=X, padx=20)

# Create Start Button
start_button = tb.Button(
    root, text="Start", bootstyle="warning outline", command=starter)
start_button.pack(pady=20)

# Create Stop Button
stop_button = tb.Button(
    root, text="Stop", bootstyle="warning outline", command=stopper)
stop_button.pack(pady=20)

# Create Increment Button
inc_button = tb.Button(root, text="Increment",
                       bootstyle="warning outline", command=increment)
inc_button.pack(pady=20)


# Create a label

my_label = tb.Label(root, text="Position: ")
my_label.pack(pady=20)

root.mainloop()
