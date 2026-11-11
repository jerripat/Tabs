from tkinter import *

root = Tk()
root.title("Listbox Example")
root.geometry("400x400")

my_frame = Frame(root)
my_frame.pack(pady=15)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)
my_scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(my_frame, width=50, yscrollcommand=my_scrollbar.set,selectmode=MULTIPLE)
listbox.pack(pady=15)
my_scrollbar.config(command=listbox.yview)

def delete():
    selected_item = listbox.curselection()
    if selected_item:
        listbox.delete(selected_item)

def select():
    selected_item = listbox.curselection()
    if selected_item:
        my_label.config(text="Selected item: " + listbox.get(selected_item))

def select_all():
    listbox.select_set(0, END)
    selected_items = listbox.curselection()
    selected_text = ", ".join([listbox.get(i) for i in selected_items])
    my_label.config(text="Selected items: " + selected_text)


items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10"]
for item in items:
    listbox.insert(END, item)

my_button= Button(root,text="Delete",command=delete)
my_button.place(x=25, y=220)
my_button2= Button(root,text="Select",command=select)
my_button2.place(x=100,y=220)
my_button3= Button(root,text="Delete All",command=lambda: listbox.delete(0, END))
my_button3.place(x=175, y=220)
my_button4= Button(root,text="Select All",command=select_all)
my_button4.place(x=260, y=220)
my_label = Label(root,text="")
my_label.pack(pady=15)
my_textbox = Text(root, width=40, height=10)
my_textbox.insert(END, "")
my_textbox.pack(pady=10)

root.mainloop()