from tkinter import *
from PIL import Image , ImageTk

root = Tk()
root.title("NewsPaper")
root.geometry("700x700")

texts=[]
photos=[]
for i in range(0,3):
    with open (f"{i+1}.txt") as f:
        text = f.read()
        texts.append(text)

    image = Image.open(f"{i+1}.png")
    # ^ Resizing the images
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root,height=70,width=800)
Label(f0,text="Times of World",font=("lucida",36,"bold")).pack()
Label(f0,text="JANUARY 19 2050",font=("lucida",16,"bold")).pack()

f0.pack()

f1 = Frame(root,width=800,height=200)
Label(f1,text=texts[0]).pack()
f1.pack()
root.mainloop()