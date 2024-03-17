from tkinter import *

root = Tk()

root.geometry("1200x1300")


root.title("Radha")

#~ Important Label Options
#* text- adds Text
#* bd - background 
#* fg - foreground color of font
#* font - sets the font (font=("comicsansms",19,"bold"))
#* padx - x axis
#* pady - y axis
#*relief - border styling - SUNKEN , RAISED , GROOVE , RIDGE

title_label = Label(text="Lorem Ipsum is simply dummy text of the printing and typesetting \nindustry. Lorem Ipsum has been the \nindustry's ",bg="purple",fg="white",padx=56,pady=26,font="comicsansms 9 bold",borderwidth=5,relief=SUNKEN)

#  Important Pack options
# anchor = "nw","ne" etc
#  side = top , bottom , left ,right
#  Fill =X or Y



title_label.pack()

root.mainloop()
