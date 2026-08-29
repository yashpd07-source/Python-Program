import tkinter as tk
def check_in():
    name = name_entry.get()
    output_text.delete("1.0", tk.END)
    output_text.insert(
        tk.END,
        f"Welcome, {name}!\n"
        "We are glad to have you at the workshop.\n"
        "Workshop Date: August 29, 2026"
    )
window = tk.Tk()
window.title("Workshop Participant Greeting")
window.geometry("500x350")
title_label = tk.Label(
    window,
    text="Workshop Participant Greeting",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)
instruction_label = tk.Label(
    window,
    text="Please enter your name and click Check In."
)
instruction_label.pack(pady=5)
name_label = tk.Label(window, text="Participant Name:")
name_label.pack()
name_entry = tk.Entry(window, width=40)
name_entry.pack(pady=5)
check_in_button = tk.Button(
    window,
    text="Check In",
    command=check_in
)
check_in_button.pack(pady=10)
output_text = tk.Text(window, width=50, height=8)
output_text.pack(pady=10)
window.mainloop()