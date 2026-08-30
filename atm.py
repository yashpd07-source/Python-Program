import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("ATM PIN Setup Interface")
root.geometry("650x600")
root.resizable(False, False)
root.configure(bg="#e8eef5")
title = tk.Label(
    root,
    text="ATM PIN Setup",
    font=("Arial", 24, "bold"),
    bg="#e8eef5",
    fg="#17365d"
)
title.place(x=205, y=20)
subtitle = tk.Label(
    root,
    text="Enter your account information and create a PIN",
    font=("Arial", 11),)