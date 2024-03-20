import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x200")
root.title("Miles to Kilometer!")

#&--------------    Heading       ------------------------------------------

title_label = ttk.Label(master=root,text="Miles to Kilometer Converter",font=("calibri",21,"bold")).pack()


root.mainloop()

