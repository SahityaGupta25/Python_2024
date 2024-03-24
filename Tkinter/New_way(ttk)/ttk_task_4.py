import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Buttons in tkinter (Time - 1:25:50)")


# ^ -----------------  Regular Button   ------------------------------------------------------------------------------



# ^ -----------------   CHeck Button     ------------------------------------------------------------------------------

check_var = tk.IntVar()

check_btn = ttk.Checkbutton(
    master=root,
    text="ARe you 18 +?",
    variable=check_var,
    
    command=lambda:print("Yes Im 18 +")
    ).pack()

# &  Instead of text varable only "variable is used as attribute while making check box"


# ^ -----------------   Radio Button    ------------------------------------------------------------------------------



radio1 = ttk.Radiobutton(master=root,text="Radio A",value='A')
radio2 = ttk.Radiobutton(master=root,text="Radio B",value='B')

exercise_check = 

# !  Value attribute is important for a radio button




root.geometry("800x400")

root.mainloop()