from tkinter import *

window = Tk()

window.title("Frames Example")
window.geometry("400x400")

frame1 = Frame(window, bg="red", width=200, height=200)
frame1.pack(padx=10, pady=10, fill=BOTH, expand=True)

frame2 = Frame(window, bg="blue", width=200, height=200)
frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)






window.mainloop()