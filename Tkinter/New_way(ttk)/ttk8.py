import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("MENU (Time - 3:31:00)")


menu = tk.Menu(master=root)
fileMenu = tk.Menu(master=menu,tearoff=False)
fileMenu.add_command(label='New', command= lambda:print('New file') )
menu.add_cascade(label='File',menu=fileMenu)
root.configure(menu=menu)


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


root.mainloop()

# * -----------------   NOTES       ------------------------------------------------------------------------------

# * Create a variable using "tk.menu()"................. menu = tk.Menu(master=root)
# * Then create file menu variable with again "tk.menu()".............. fileMenu = tk.Menu(master=root,tearoff=False)
# * Then write this............. menu.add_cascade(label='File',menu=fileMenu)
# * Then to create a Sub Menu write this 
# * root.configure(menu=menu)
# *
# *
# *
# *
# *