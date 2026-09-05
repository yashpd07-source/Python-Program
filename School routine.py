import tkinter as tk
from tkinter import messagebox
routine = [
    "Do homework",
    "Eat a snack",
    "Take a break",
    "Finish chores",
    "Get ready for tomorrow"
]
current_task = 0
# Shows the last character typed
def show_last_character(event):
    text = task_entry.get()
    if text:
        last_character_label.config(
            text="Last character typed: " + text[-1]
        )
    else:
        last_character_label.config(
            text="Last character typed: None"
        )
def routine_clicked(event):
    click_label.config(
        text="You clicked the routine area!"
    )
def check_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning(
            "No Task",
            "Please enter a task first!"
        )
    else:
        result_label.config(
            text="Task entered: " + task
        )
def next_task():
    global current_task
    task_label.config(
        text="Next task: " + routine[current_task]
    )
    current_task += 1
    if current_task >= len(routine):
        current_task = 0
window = tk.Tk()
window.title("After-School Routine Checker")
window.geometry("600x500")
window.configure(bg="#f4f7fb")
title_label = tk.Label(
    window,
    text="After-School Routine Checker",
    font=("Arial", 24, "bold"),
    bg="#f4f7fb",
    fg="#243b53"
)
title_label.pack(pady=20)
instructions = tk.Label(
    window,
    text="Enter an after-school task below:",
    font=("Arial", 14),
    bg="#f4f7fb",
    fg="#486581"
)
instructions.pack(pady=5)
task_entry = tk.Entry(
    window,
    font=("Arial", 16),
    width=35
)
task_entry.pack(pady=10)
task_entry.bind("<KeyRelease>", show_last_character)
last_character_label = tk.Label(
    window,
    text="Last character typed: None",
    font=("Arial", 13),
    bg="#f4f7fb",
    fg="#334e68"
)
last_character_label.pack(pady=5)
check_button = tk.Button(
    window,
    text="Check Task",
    font=("Arial", 13, "bold"),
    bg="#4f86c6",
    fg="white",
    width=15,
    command=check_task
)
check_button.pack(pady=10)
routine_frame = tk.Frame(
    window,
    bg="#d9eaf7",
    width=450,
    height=120,
    highlightbackground="#4f86c6",
    highlightthickness=2
)
routine_frame.pack(pady=15)
routine_frame.pack_propagate(False)
routine_title = tk.Label(
    routine_frame,
    text="Routine Area\n(Click here!)",
    font=("Arial", 18, "bold"),
    bg="#d9eaf7",
    fg="#243b53"
)
routine_title.pack(expand=True)
routine_frame.bind("<Button-1>", routine_clicked)
routine_title.bind("<Button-1>", routine_clicked)
click_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    bg="#f4f7fb",
    fg="#2f855a"
)
click_label.pack(pady=5)
task_label = tk.Label(
    window,
    text="Next task: Click the button below",
    font=("Arial", 15, "bold"),
    bg="#f4f7fb",
    fg="#243b53"
)
task_label.pack(pady=10)
next_button = tk.Button(
    window,
    text="Next Task",
    font=("Arial", 13, "bold"),
    bg="#2f855a",
    fg="white",
    width=15,
    command=next_task
)
next_button.pack(pady=5)
window.mainloop()