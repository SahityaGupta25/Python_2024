import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Getting and setting widgets (Time - 1:03:00)")
root.geometry("800x400")

string_var = tk.StringVar()

my_label = ttk.Label(master=root,textvariable=string_var)
my_label.pack()

my_entry = ttk.Entry(master=root,textvariable=string_var)
my_entry.pack()

root.mainloop()