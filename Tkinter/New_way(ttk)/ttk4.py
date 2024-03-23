import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Buttons in tkinter (Time - 1:06:50)")

str_var = tk.StringVar(value="Btn.ttk()")

btn_ttk = ttk.Button(master=root,text="Click Me!",command=lambda:print("Hey its me"),textvariable=str_var).pack()

def check_kar():
    print(check_var.get())

check_var = tk.IntVar()
check_bttn= ttk.Checkbutton(master=root,text="Check box Demo",variable=check_var,command=check_kar).pack()

root.geometry("800x400")



root.mainloop()