from tkinter import *
from tkinter import font
# Imported font
from PIL import Image , ImageTk
root = Tk()



root.geometry("1260x900")

# ? Min & Max Size      -------------------------------
root.minsize(400,600)

root.maxsize(1600,900)
# ?------------------------------------------------


the = Label(text="THE",font=("Courier New",36,"bold"))
the.pack()

#^ AI Image     ---------------------------------------------
ai2_image= PhotoImage(file="./IMG/ai2.png")
ai2_label = Label(image=ai2_image)
ai2_label.pack()


ai3_image= PhotoImage(file="./IMG/ai3.png")
ai3_resize = ai3_image.resize((300,200),Image.ANTIALIAS)
ai3_label = Label(image=ai3_image)
ai3_label.pack()
# ^ ----------------------------------------------------------

times = Label(text="TIMES",font=("Courier New",36,"bold"))
times.pack()

x = Label(text="Meet Devin, World's 1st AI Software Engineer Who Can Build Websites, Videos From A Prompt")
x.pack()


root.mainloop()