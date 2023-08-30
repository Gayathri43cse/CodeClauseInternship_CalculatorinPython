import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password():
    try:
        password_length = int(length_entry.get())
        random_password = generate_random_password(password_length)
        result_label.config(text="Random Password: " + random_password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length.")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry('300x100')

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
