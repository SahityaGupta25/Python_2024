import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Buttons in tkinter (Time - 1:06:50)")


# ^ -----------------  Regular Button   ------------------------------------------------------------------------------
str_var = tk.StringVar(value="Btn.ttk()")
btn_ttk = ttk.Button(master=root,text="Click Me!",command=lambda:print("Hey its me"),textvariable=str_var).pack()


# ^ -----------------   CHeck Button     ------------------------------------------------------------------------------
def check_kar():
    print(check_var.get())

# &  Instead of text varable only "variable is used as attribute while making check box"
check_var = tk.IntVar()
check_bttn= ttk.Checkbutton(master=root,text="Check box Demo",variable=check_var,command=check_kar,onvalue=10,offvalue=5).pack()

# ^ -----------------   Radio Button    ------------------------------------------------------------------------------

# !  Value attribute is important for a radio button


radio_var = tk.StringVar()

radio1 = ttk.Radiobutton(
    root,
    text="one",
    value="hi",
    variable=radio_var,
    command= lambda:print(radio_var.get())
    ).pack()
radio2 = ttk.Radiobutton(
    root,
    text="two",
    value="hello",
    variable=radio_var,
    command= lambda:print(radio_var.get())
    ).pack() 

root.geometry("800x400")

# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------


root.mainloop()