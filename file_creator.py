import tkinter as tk
from tkinter import simpledialog, messagebox
import os

def create_files():
    folder_name = simpledialog.askstring("Input", "Enter folder name:")
    if not folder_name:
        return

    file_name = simpledialog.askstring("Input", "Enter Python file name:")
    if not file_name:
        return

    if not file_name.endswith(".py"):
        file_name += ".py"

    os.makedirs(folder_name, exist_ok=True)

    with open(os.path.join(folder_name, file_name), 'w') as f:
        f.write("# This is a new Python file")

    messagebox.showinfo("Success", f"Created {file_name} inside {folder_name}!")

root = tk.Tk()
root.withdraw()  # Hide the main window

create_files()