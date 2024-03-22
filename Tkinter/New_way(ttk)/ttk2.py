import tkinter as tk

window = tk.Tk()
window.geometry("800x600")

text_1 = tk.Text(master=window)
text_1.pack()
window.mainloop()