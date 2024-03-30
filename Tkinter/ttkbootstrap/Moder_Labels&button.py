import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *


# root = tk.Tk()
root = tb.Window(themename='superhero')
root.title("Modern Labels and buttons")
root.geometry("800x400")

label_one = tb.Label(root,text="Hello!",font=("Arial",66),bootstyle = 'danger inverse')
label_one.pack(pady=50)

count = 0
def changeColor():
    global count
    count +=1 
    if count %2 ==0:
        label_one.config(text="Hare Ram")
    else:
        label_one.config(text="Sita Ram")


btn = tb.Button(root,text="Click Me!",bootstyle = 'success, outline',command=changeColor)
btn.pack()


root.mainloop()
# * Instead of tk.Tk() use root = tb.window()
# * we can add theme by writing root = tb.window(themename = theme_name)
# *
# *
# *