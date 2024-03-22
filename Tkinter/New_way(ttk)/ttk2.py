import tkinter as tk
from tkinter import ttk 

window = tk.Tk()
window.title("Window & Widgets")
window.geometry("800x600")

# ^ -----------  ttk text -------------
text_1 = tk.Text(master=window)
text_1.pack()


# ^ -----------  ttk label -------------
label_1 = ttk.Label(master=window,text="This is a test")
label_1.pack()






window.mainloop()