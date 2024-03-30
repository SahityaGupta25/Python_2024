import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *


# root = tk.Tk()
root = tb.Window(themename='superhero')
root.title("Modern Labels and buttons")
root.geometry("800x400")

label_one = tb.Label(root,text="Hello!",font=("Arial",66),bootstyle = 'danger inverse')
label_one.pack()
root.mainloop()

# * Instead of tk.Tk() use root = tb.window()
# * we can add theme by writing root = tb.window(themename = theme_name)
# *
# *
# *