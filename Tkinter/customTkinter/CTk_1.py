from customtkinter import *
from PIL import Image 

root = CTk()
root.geometry("700x700")
set_appearance_mode("dark")
root.title("First Custom APP")
img = Image.open("ai3.png")
btn = CTkButton(master=root,text="Click ME",corner_radius=30,image=CTkImage(dark_image=img,light_image=img))
btn.place(relx="0.3",rely="0.6")
root.mainloop()


# * What I have learnt
# * Corner radius
# * set_apperance_mode(" ")
# * border_color & border_width