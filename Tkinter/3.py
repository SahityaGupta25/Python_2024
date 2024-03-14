from tkinter import *
from PIL import Image , ImageTk

root = Tk()

root.geometry("1300x1200")

# photo = PhotoImage(file="ss.png")

# ! For JPG Images (install pillow and import Image , ImageTk)

image = Image.open("bmw.jpg")
photo = ImageTk.PhotoImage(image)

img_label = Label(image=photo)
img_label.pack()

root.mainloop()

