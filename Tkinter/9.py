from tkinter import *
root = Tk()
root.geometry("1200x900")

# ^ Heading
label_1 = Label(root,text="Fill the form & Sign Up",font=("Helvetica" ,16 ,"bold"),pady=40).grid(row=0,column=3)

# ^ Text for our inputs in form
name = Label(root,text="Name",font=("Helvetica",11,"normal"))
phone = Label(root,text="Phone",font=("Helvetica",11,"normal"))
gender = Label(root,text="Gender",font=("Helvetica",11,"normal"))
emergency = Label(root,text="Emergency Contact",font=("Helvetica",11,"normal"))
paymentmode = Label(root,text="Payment mode",font=("Helvetica",11,"normal"))


# ^ Packed through gridname.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

#^ tkinter variable for storing entries
name_val = StringVar()
phone_val = IntVar()
gender_val = StringVar()
emergency_val = StringVar()
pay_val = IntVar()
food_service_val = StringVar()

# ^ Input for our form
name_entry = Entry(root,textvariable=name_val)
phone_entry = Entry(root,textvariable=phone_val)
gender_entry = Entry(root,textvariable=gender_val)
emergency_entry = Entry(root,textvariable=emergency_val)
payment_entry = Entry(root,textvariable=pay_val)

# ^ Packed through grid
name_entry.grid(row=1,column=3)
phone_entry.grid(row=2,column=3)
gender_entry.grid(row=3,column=3)
emergency_entry.grid(row=4,column=3)
payment_entry.grid(row=5,column=3)

root.mainloop()






#* STEPS
# *
# *
# *
# *
# *
# *
# *
# *
