import tkinter as tk
from tkinter import ttk


count = 0

def clicked(): # without event because I use `command=` instead of `bind`
    global count

    count = count + 1

    label1.configure(text=f'{count} accounts completed')


windows = tk.Tk()
windows.title("Click Counter")

label = tk.Label(windows, text="Click for each account completed")
label.grid(column=0, row=0)

label1 = tk.Label(windows)
label1.grid(column=0, row=1)

custom_button = ttk.Button(windows, text="Add", command=clicked)
custom_button.grid(column=1, row=1)

windows.mainloop()