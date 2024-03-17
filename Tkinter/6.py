from tkinter import *

root = Tk()

root.geometry("900x900")

f1 = Frame(root,bg="grey",borderwidth=9,relief=SUNKEN)
f1.pack(side=LEFT)

f1_label = Label(f1,text="Jai bhole ki")
f1_label.pack(pady=42)
root.mainloop()