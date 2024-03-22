import tkinter as tk
from tkinter import ttk 

def btn_func():
    print("Button is pressed")

window = tk.Tk()
window.title("Window & Widgets")
window.geometry("800x600")
# ^ -----------  ttk label -------------
label_1 = ttk.Label(master=window,text="This is a test")
label_1.pack()

# ^ -----------  ttk text -------------
text_1 = tk.Text(master=window)
text_1.pack()

# ^ -----------  ttk entry -------------

entry_1 = ttk.Entry(master=window)
entry_1.pack()

# ^ -----------  ttk button -------------

button_1 = ttk.Button(master=window,text="CLick Me!",command=btn_func)
button_1.pack()


window.mainloop()