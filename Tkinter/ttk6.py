import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Events in tkinter (Time - 1:44:40)")
root.geometry("800x800")

# ^ -----------------   TEXT      ------------------------------------------------------------------------------

text = tk.Text(root).pack()

# ^ -----------------   ENTRY       ------------------------------------------------------------------------------

entry = ttk.Entry(root)
entry.pack()

# ^ -----------------   Button       ------------------------------------------------------------------------------

btn = ttk.Button(master=root,text="BTN")
btn.pack()

# ^ -----------------   EVENTS       ------------------------------------------------------------------------------
#! SYNTAX
#~      root.bind(event,function)
# ~     root.bind('modifier-type-detail', lambda : print('an event'))


btn.bind('<Alt-KeyPress-a>',lambda event: print(event))

# ^ -----------------   Root Events       ------------------------------------------------------------------------------

def get_pos(event):
    print(f"x:{event.x} y: {event.y}")

#! root.bind('<Motion>',get_pos)
#! root.bind('<KeyPress>',lambda event : print(f"Btn was pressed .............. {event.char}"))

entry.bind('<FocusIn>',lambda event : print('Entry field was selected',event))
entry.bind('<FocusOut>',lambda event : print('Entry field was selected',event))


# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------
# ^ -----------------   ENTRY       ------------------------------------------------------------------------------


root.mainloop()