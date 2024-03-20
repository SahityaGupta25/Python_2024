from tkinter import *
from PIL import Image , ImageTk

root = Tk()

root.geometry("700x700")

def harry(event):
    print(f"Clicked {event.x} & {event.y}")

widget1 = Button(root,text="Click Me!")
widget1.grid(row=1,column=4)

widget1.bind('<Button-1>',harry)        #^  (Event,function)



root.mainloop()