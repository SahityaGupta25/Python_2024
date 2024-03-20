import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x140")
root.title("Miles to Kilometer!")

# ~  --------------------    Convert Function    --------------------------------------------------------------

def  convert():
    print(input_entry.get())

# ~   ---------------------------------------------------------------------------------------------------------

#&--------------    Heading (Label)     -----------------------------------------------------------------------

title_label = ttk.Label(master=root,text="Miles to Kilometer Converter",font=("calibri",21,"bold")).pack()

# & --------------------------------------------------------------------------------------------------------

# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
input_frame = ttk.Frame(master=root )
input_entry =  ttk.Entry(master=input_frame)
input_button = ttk.Button(master=input_frame,text="Convert",command=convert)
input_entry.pack(side="left",padx=10)
input_button.pack(side="left")
input_frame.pack(pady=10)

# ^ --------------------------------------------------------------------------------------------------------------

#!  ------------------- Output Label ------------------------------------------------------------------------------

output_label = ttk.Label(master=root,text="Output", font=("Arial",16,"normal"))
output_label.pack(pady=5)

#!  ---------------------------------------------------------------------------------------------------------------

root.mainloop()

