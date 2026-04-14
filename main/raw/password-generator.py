import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_var.get())
        chars = string.ascii_letters
        if digits_var.get():
            chars += string.digits
        if symbols_var.get():
            chars += string.punctuation

        if length <= 0:
            raise ValueError("Length must be positive")

        password = ''.join(random.choice(chars) for _ in range(length))
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(bg="#1e1e2f")

# Variables
length_var = tk.StringVar(value="12")
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

# Title
title_label = tk.Label(root, text="🔐 Password Generator", font=("Arial", 16, "bold"), fg="white", bg="#1e1e2f")
title_label.pack(pady=10)

# Length input
length_frame = tk.Frame(root, bg="#1e1e2f")
length_frame.pack(pady=5)
tk.Label(length_frame, text="Length:", font=("Arial", 12), fg="white", bg="#1e1e2f").pack(side="left")
tk.Entry(length_frame, textvariable=length_var, width=5).pack(side="left")

# Options
options_frame = tk.Frame(root, bg="#1e1e2f")
options_frame.pack(pady=5)
tk.Checkbutton(options_frame, text="Include Digits", variable=digits_var, font=("Arial", 12), fg="white", bg="#1e1e2f", selectcolor="#2e2e3f").pack(anchor="w")
tk.Checkbutton(options_frame, text="Include Symbols", variable=symbols_var, font=("Arial", 12), fg="white", bg="#1e1e2f", selectcolor="#2e2e3f").pack(anchor="w")

# Generate button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
generate_btn.pack(pady=10)

# Password display
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30, justify="center")
password_entry.pack(pady=5)

# Copy button
copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="#2196F3", fg="white")
copy_btn.pack(pady=10)

root.mainloop()
