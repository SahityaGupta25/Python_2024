from customtkinter import *
from PIL import Image 

root = CTk()
root.geometry("700x700")
set_appearance_mode("dark")


label_1 = CTkLabel(master=root,text="RAM RAM LADD LE",text_color="crimson",font=("Arial",19) )
label_1.place(relx="0.5",rely="0.5",anchor="center")

combo_box = CTkComboBox(master=root,values= ["Rajput","Gujjar","Jaat","Yadav","Pandat","Baniya"],dropdown_fg_color="crimson",border_width=2,border_color="crimson")
combo_box.place(relx="0.6",rely="0.6",anchor="center")

root.mainloop()


# * What I have learnt
# * dropdwon widget
# * combo box widget
# *
# *
# *
# *
# *
# *