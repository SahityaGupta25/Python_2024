from tkinter import *
root = Tk()
def getvals():
    print(user_var.get())
    print(pass_var.get())

root.geometry("1300x900")
root.title("GRID layout & Entry Widget")

user_label = Label(root,text="Username")
password_label = Label(root,text="password")
user_label.grid()
password_label.grid()

user_var = StringVar()
pass_var = StringVar()

user_entry = Entry(root,textvariable=user_var)
pass_entry = Entry(root,textvariable=pass_var)

user_entry.grid(row=0,column=1)
pass_entry.grid(row=1,column=1)

Button(text="Submit",command=getvals).grid()

root.mainloop()