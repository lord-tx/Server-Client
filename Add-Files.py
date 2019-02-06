import tkinter as tk
import os
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext as scr


win = tk.Tk()
win.minsize(200, 200)
win.resizable(0,0)
win.title("Test Add Button")

display_box = scr.ScrolledText(win, width=60, height=10)
display_box.grid(column=1, row=1, sticky=tk.NSEW)

folder_list = []

# This function is to enable the user add folders to be accessed
def add_folder():
    # some highlighted variables are for test purposes only

    folder_variable = filedialog.askdirectory(parent=win, initialdir='C:\\User', title='Select your Music and Videos folder')
    ## print(folder_variable)
    # display_box.insert(tk.INSERT, folder_variable)
    folder_list.append(folder_variable)
    ## print(folder_list)
    ## display_box.insert(tk.INSERT, folder_list)


def display_folder_contents():
    j=0
    files = os.walk(folder_list[j])
    j = j+1
    for i in files:
        display_box.insert(tk.INSERT, i)
        print(i, "\n")


add_button = ttk.Button(win, text="Add Folder", command = add_folder)
add_button.grid(column=0, row=1)

view_button = ttk.Button(win, text="View Files", command = display_folder_contents)
view_button.grid(column=2, row=1)

win.mainloop()
