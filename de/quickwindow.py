import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo as si
import os
import time

path_to_de = os.path.dirname(os.path.abspath(__file__))

def is_first_open(path):
    with open(f"{path}/de_cfg/first_open.txt", "r") as f:
        is_first = f.readline().strip()
    return is_first == "1"

def loading():
    loading_window = tk.Toplevel()
    loading_window.title("Loading...")
    loading_window.geometry("300x300")
    
    progress = ttk.Progressbar(loading_window, orient="horizontal", length=150, value=0, maximum=100)
    progress.pack(pady=5)
    install_logs = tk.Label(loading_window, text="")
    install_logs.pack()
    
    
    progress['value'] = 0
    install_logs["text"] = "Loading..."
    loading_window.update_idletasks()
    time.sleep(1)

    progress['value'] = 25
    install_logs["text"] = "Loading..."
    loading_window.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    install_logs["text"] = "Loading..."
    loading_window.update_idletasks()
    time.sleep(1)

    progress['value'] = 75
    install_logs["text"] = "Loading..."
    loading_window.update_idletasks()
    time.sleep(1)

    progress['value'] = 100
    install_logs["text"] = "Loading..."
    loading_window.update_idletasks()
    time.sleep(1)
    loading_window.destroy()

default_font = ("Consolas", 11)

desktop = tk.Tk()
desktop.title("QuickWindow")
desktop.geometry("1920x1080")

is_first = is_first_open(path_to_de)

# Upper Menu
menu_bar = tk.Menu(desktop)
desktop.config(menu=menu_bar)


upper_menu = tk.Menu(menu_bar, tearoff=0) 
menu_bar.add_cascade(label="Test", menu=upper_menu)
#upper_menu.add_command(label="Open", command=create_open_window)
upper_menu.add_separator()
upper_menu.add_command(label="Exit", command=desktop.quit)

loading()

if is_first == 1:
    si(title="First launch info", message="Welcome to the QuickWindow DE! Enjoy this ugly interface)")
    with open(f"{path_to_de}/de_cfg/first_open.txt", "w") as f:
        f.write("0")

# Labels, buttons, and more...

name = tk.Label(desktop, text="QuickWindow v.0.6.1")
name.pack(pady=5)


desktop.mainloop()