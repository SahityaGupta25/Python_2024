import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("MENU (Time - 3:31:00)")


# ^ -----------------   MENU       ------------------------------------------------------------------------------
menu = tk.Menu(master=root)
# ^ -----------------   Sub-Menu       ------------------------------------------------------------------------------
fileMenu = tk.Menu(master=menu,tearoff=False)
fileMenu.add_command(label='New', command= lambda:print('New file') )
fileMenu.add_command(label='Open',command= lambda:print('Open File'))
menu.add_cascade(label='File',menu=fileMenu)

# ^ -----------------  Another Sub-Menu      ------------------------------------------------------------------------------

helpFileMenu = tk.Menu(menu,tearoff=False)
helpVar = tk. StringVar()
helpFileMenu.add_command(label='You need Help',command = lambda : print("Help!"))
helpFileMenu.add_checkbutton(label="Check",onvalue='on',offvalue='off',variable=helpVar)
menu.add_cascade(label='Help',menu=helpFileMenu)

root.geometry("800x400")
root.configure(menu=menu)

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