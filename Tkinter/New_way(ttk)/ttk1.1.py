import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


root = ttk.Window(themename="darkly")  # journal
root.geometry("400x180")
root.title("Miles to Kilometer!")

# ~  --------------------    Convert Function    --------------------------------------------------------------

def  convert():
    mile_input = input_entry_int.get()
    km_output = mile_input * 1.61 
    output_string.set(f"{km_output} Km/hr")


# ~   ---------------------------------------------------------------------------------------------------------

#&--------------    Heading (Label)     -----------------------------------------------------------------------

title_label = ttk.Label(master=root,text="Miles to Kilometer Converter",font=("calibri",21,"bold")).pack()

# & --------------------------------------------------------------------------------------------------------

# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
input_frame = ttk.Frame(master=root )
input_entry_int = tk.IntVar()
input_entry =  ttk.Entry(master=input_frame,textvariable=input_entry_int)
input_button = ttk.Button(master=input_frame,text="Convert",command=convert)
input_entry.pack(side="left",padx=10)
input_button.pack(side="left")
input_frame.pack(pady=10)

# ^ --------------------------------------------------------------------------------------------------------------

#!  ------------------- Output Label ------------------------------------------------------------------------------
output_string = tk.StringVar()
output_label = ttk.Label(master=root,text="Output", font=("Arial",16,"normal"),textvariable=output_string)
output_label.pack(pady=5)

#!  ---------------------------------------------------------------------------------------------------------------

root.mainloop()

