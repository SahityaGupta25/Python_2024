import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Buttons in tkinter (Time - 1:06:50)")


btn_ttk = ttk.Button(master=root,text="Click Me!",command=lambda:print("Hey its me")).pack()


root.geometry("800x400")



root.mainloop()