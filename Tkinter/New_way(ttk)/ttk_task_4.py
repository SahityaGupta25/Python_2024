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

# &  Instead of text variable only "variable" is used as attribute while making check box"


# ^ -----------------   Radio Button    ------------------------------------------------------------------------------
def radio_func():
    print(f"{check_var.get()}")
    check_var.set(False)

radio_var = tk.StringVar()      #& Using string var because value are also in string
Check_var = tk.BooleanVar()

radio1 = ttk.Radiobutton(master=root,text="Radio A",value='A',variable=radio_var,command=radio_func)
radio2 = ttk.Radiobutton(master=root,text="Radio B",value='B',variable=radio_var,command=radio_func)

exercise_check = ttk.Checkbutton(root,text="Exercise Check",variable=check_var,command=lambda: print(radio_var.get()))
radio1.pack()
radio2.pack()
exercise_check.pack()

# !  Value attribute is important for a radio button




root.geometry("800x400")

root.mainloop()