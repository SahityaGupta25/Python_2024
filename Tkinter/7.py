from tkinter import *
root = Tk()
root.geometry("1200x600")
root.title("Buttons in Tkinter")

def printing():
    print("Printing............")

frame1 = Frame(root,borderwidth=6,bg="grey",relief=RAISED)
frame1.pack(side=LEFT,anchor="nw")

btn1 = Button(frame1,fg="red",text="Print Now",command=printing)
btn1.pack(side=LEFT)
btn2 = Button(frame1,fg="brown",text="Print Now")
btn2.pack(side=LEFT)
btn3 = Button(frame1,fg="green",text="Print Now")
btn3.pack(side=LEFT)

root.mainloop()