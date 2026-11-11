
import tkinter as tk
import webbrowser


def open_link(event):
    webbrowser.open("https://en.wikipedia.org/wiki/Python_(programming_language)")


root = tk.Tk()
root.title("Tkinter Hyperlink Example")
root.geometry("500x300")

# Create Text widget
textbox = tk.Text(
    root,
    font=("Arial", 14),
    width=45,
    height=10,
    wrap="word"
)
textbox.pack(padx=20, pady=20)

# Insert regular text
textbox.insert(tk.END, "Welcome to my Python application!\n\n")
textbox.insert(tk.END, "Visit the Python website: ")

# Insert hyperlink
textbox.insert(tk.END, "Python_(programming_language)", "hyperlink")

# Configure hyperlink appearance
textbox.tag_config(
    "hyperlink",
    foreground="blue",
    underline=True
)

# Make hyperlink clickable
textbox.tag_bind(
    "hyperlink",
    "<Button-1>",
    open_link
)

# Change mouse cursor when hovering
textbox.tag_bind(
    "hyperlink",
    "<Enter>",
    lambda event: textbox.config(cursor="hand2")
)

textbox.tag_bind(
    "hyperlink",
    "<Leave>",
    lambda event: textbox.config(cursor="xterm")
)

# Prevent editing
textbox.config(state="disabled")

root.mainloop()
