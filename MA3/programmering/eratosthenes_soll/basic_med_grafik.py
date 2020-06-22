#!/bin/python

import tkinter as tk

numlist = []
resultat = []

canvas_height = 700
canvas_width = 700

frame_bg = "blue"
frame_relx = 0.1
frame_rely = 0.1
frame_relheight = 0.8
frame_relwidth = 0.8

label_ipadx = 5
label_ipady = 5
label_padx = 3
label_pady = 3

numwidth = 4

root = tk.Tk()
root.wm_title("Erastothenes soll")

canvas = tk.Canvas(root, height=canvas_height, width=canvas_width)
canvas.pack()

frame = tk.Frame(root, bg=frame_bg)
frame.place(relx=frame_relx, rely=frame_rely, relwidth=frame_relwidth, relheight=frame_relheight)

# button = tk.Label(frame, text="label0", bg='yellow')
# button.grid(column=0, row=0, ipadx=label_ipadx, ipady=label_ipady, padx=label_padx, pady=label_pady)

# label1 = tk.Label(frame, text="label1", bg="yellow")
# label1.grid(column=1, row=0, ipadx=label_ipadx, ipady=label_ipady, padx=label_padx, pady=label_pady)

# label2 = tk.Label(frame, text="label2", bg="yellow")
# label2.grid(column=2, row=0, ipadx=label_ipadx, ipady=label_ipady, padx=label_padx, pady=label_pady)

# label3 = tk.Label(frame, text="label3", bg="yellow")
# label3.grid(column=3, row=0, ipadx=label_ipadx, ipady=label_ipady, padx=label_padx, pady=label_pady)

def genlabel(curr_num, j):
    print(j)
    tk.Label(frame, text=curr_num, bg="yellow").grid(column=0, row=curr_num, ipadx=label_ipadx, ipady=label_ipady, padx=label_padx, pady=label_pady)


# Eratosthenes soll:
# Ideen är att loopa igenom listan med variabeln "i" och testa om "j" är delbart med "i"
# Är "j" delbart med "i" ska "i" tas bort ifrån listan.

j = 0
numlist = []
limit = 50

# Generering av listan:
for i in range(2, limit): # man måste börja med två
    numlist.append(i)


# Själva sollet:
for i in numlist:

    genlabel(i)

    for j in numlist:
        if j == i:
            continue

        elif not(j % i):
            numlist.remove(j)


print("resultat: ", numlist)



root.mainloop()
