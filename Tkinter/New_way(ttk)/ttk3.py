import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry_ttk.get()

    # ! Update the label using config
    my_label['text'] = entry_text

root = tk.Tk()
root.title("Getting and setting widgets (Time - 42:05)")
root.geometry("800x400")

my_label = ttk.Label(master=root,text="This is my Label")
my_label.pack()

entry_ttk = ttk.Entry(master=root)
entry_ttk.pack()

btn = ttk.Button(master=root,text="Click Me!",command=button_func)
btn.pack()


root.mainloop()