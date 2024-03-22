import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry_ttk.get()

    # ! Update the label using config
    my_label['text'] = entry_text

def button2_func():
    entry_revert = entry_ttk.get()
    my_label.config(text="some text")
    my_label.config(state="enabled")

root = tk.Tk()
root.title("Getting and setting widgets (Time - 42:05)")
root.geometry("800x400")

my_label = ttk.Label(master=root,text="This is my Label")
my_label.pack()

entry_ttk = ttk.Entry(master=root)
entry_ttk.pack()

btn = ttk.Button(master=root,text="Click Me!",command=button_func)
btn.pack()
btn2 = ttk.Button(master=root,text="Revert",command=button2_func)
btn2.pack()



root.mainloop()