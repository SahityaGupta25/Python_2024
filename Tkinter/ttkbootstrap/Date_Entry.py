import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

root = tk.Tk()
root.title("Calendar using bootStarp")
root.geometry("800x400")



my_date = tb.DateEntry(root,bootstyle='danger')
my_date.pack()

root.mainloop()