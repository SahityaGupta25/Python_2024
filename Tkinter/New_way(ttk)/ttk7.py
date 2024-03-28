import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Combo box & Spin Box in tkinter (Time - 1:54:00) ")

# ^ -----------------   COMBO BOX       ------------------------------------------------------------------------------

items = ('Coconut','Pan Cake','Sandwich','Manchurian')
comboVar = tk.StringVar(value=items[2])
combo_box=ttk.Combobox(root,textvariable=comboVar)
#! combo_box['values'] = items
combo_box.configure(values=items)
combo_box.pack()

# ^ -----------------   COMBO BOX EVENTS       ------------------------------------------------------------------------------

combo_box.bind('<<ComboboxSelected>>',lambda event : print(comboVar.get()))

comboLabel = ttk.Label(root,text='A Label',textvariable=comboVar)
comboLabel.pack()

# ^ -----------------   SPIN BOX      ------------------------------------------------------------------------------

spin_var = tk.IntVar(value=16)

#~ numberList = (25,16,2,66,29)
spinBox = ttk.Spinbox(root,from_=66,to=166,increment=10,textvariable=spin_var)
#~ spinBox['value'] = numberList
spinBox.bind('<<Increment>>',
lambda event : print('Value are increasing'),

)
spinBox.bind('<<Decrement>>',
lambda event : print('Value are decreasing'),

)
spinBox.pack()

root.geometry("800x400")

# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------


root.mainloop()

# * -----------------   NOTES       ------------------------------------------------------------------------------
# * Combo box is nothing but a drop down menu
# * Spin Box is a menu of pre defined value 
# * Combo Box uses text variable
# *
# *
# *