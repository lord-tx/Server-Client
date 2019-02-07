
import tkinter as tk                        # For tkinter Widgets
import os                                   # For access to os properties such as path
from tkinter import ttk                     # Themed tkinter for beautiful interfaces
from tkinter import filedialog              # Tkinter file dialog interface.
from tkinter import scrolledtext as scr     # Scrolled Text Widget

# TODO: Recreate into a GUI class

win = tk.Tk()
win.minsize(200, 200)           # Allows us to hold the application at a definite size
win.resizable(0,0)              # Prevents increasing the size of the widget unless forced
win.title("Test Add Button")    # Could be changed on any 'Test Commit'

"""Display Box is Global cause of it's accessibility on various levels"""

# TODO: Rephrase into a modular program

display_box = scr.ScrolledText(win, width=60, height=10)
display_box.grid(column=1, row=1, sticky=tk.NSEW)


"""Folder list is an actual folder list"""
folder_list = []

# This function is to enable the user add folders to be accessed
def add_folder():
    """"This function is to enable the user add folders to be accessed"""

    # some highlighted variables are for test purposes only

    """ I was finally able to make it default to HOME anytime by using 'tilde' '~' in 'initial dir'"""

    folder_variable = filedialog.askdirectory(parent=win, initialdir='~', title='Select your Music and Videos folder')
    ## print(folder_variable)
    # display_box.insert(tk.INSERT, folder_variable)
    folder_list.append(folder_variable)
        # Button = tk.Button(win, text="[]".format(folder_name), width=10, command=display_folder_contents)
        # Button.grid(column=4, row=k)
        # k += 1
    ## print(folder_list)
    ## display_box.insert(tk.INSERT, folder_list)


def display_folder_contents():
    j = 0
    while j<len(folder_list):
        selected_folder = os.listdir(folder_list[j])
        j = j + 1
        for i in selected_folder:
            # TODO: Fix the Display Box Output and organize it.
            # This activity of displaying the output into an scrolled text widget
            # comes out warped

            ## 'display_box.insert(tk.INSERT, i, "\n")'

            print(i, )

            # TODO: Fix the sub_folder selction and redirect output accordingly
        # actual_file_list = selected_folder[j]
        # print("The Contents of {} are: \n{}\n".format(selected_folder, actual_file_list))
        # sprint(actual_file_list, "\n")

            # TODO: Consider deleting these final lines
    #for i in files:

    #    display_box.insert(tk.INSERT, i)
    #    print(i, "\n")

""" Two test buttons created for the test processes. """
add_button = ttk.Button(win, text="Add Folder", command = add_folder)
add_button.grid(column=0, row=1, sticky=tk.N)

view_button = ttk.Button(win, text="View Files", command = display_folder_contents)
view_button.grid(column=0, row=1, sticky=tk.S)

# TODO: Mainloop is just for the test phase
win.mainloop()

"""
if __name__ == '__main__':          # This prototype would be used instead.
    win.mainloop()
"""

# TODO: Rephrase everything into modules at the end of testing phase.