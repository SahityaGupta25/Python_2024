import tkinter as tk
from tkinter import ttk

def btn():
    print("Hello")

root = tk.Tk()
root.title("Task 1")
root.geometry("800x400")

entry_ttk = ttk.Entry(master=root)
entry_ttk.pack()

my_label = ttk.Label(master=root,text="This is my Label")
my_label.pack()

btn = ttk.Button(master=root,text="Click Me!",command=btn)
btn.pack()


root.mainloop()