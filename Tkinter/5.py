from tkinter import *
from tkinter import font
# Imported font
root = Tk()



root.geometry("600x900")

root.minsize(400,600)

root.maxsize(1500,700)

the = Label(text="THE",font=("Courier New",36,"bold"))
the.pack()

times = Label(text="TIMES",font=("Courier New",36,"bold"))
times.pack()

x = Label(text="Meet Devin, World's 1st AI Software Engineer Who Can Build Websites, Videos From A Prompt")
x.pack()


root.mainloop()