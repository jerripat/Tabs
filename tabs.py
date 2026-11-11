from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=1, fill="both")
Label(tab1, text="This is Tab 1",width=50, height=25).pack(pady=20)
Label(tab2, text="This is Tab 2",width=50, height=25).pack(pady=20)

window.mainloop()