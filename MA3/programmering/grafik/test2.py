#!/bin/python

from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        exit_button = Button(self, text="Exit", command = self.click_exit_button)
        exit_button.place(x=0, y=0)

        self.pack(fill=BOTH, expand=1)

    def click_exit_button(self):
        exit()

# Intialisering
root = Tk()
app = Window(root)

root.geometry("400x400")

# Fönstertitel
root.wm_title("Hello World")

# Visa fönstret
root.mainloop()
