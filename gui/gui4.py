import tkinter as tk


def display1(event):
    print("single click")


def display2(event):
    print("double click")


root = tk.Tk()
Button1 = tk.Button(root, text="Press Me")
Button1.pack(side=tk.LEFT)

Button1.bind("<Button-1>", display1)
Button1.bind("<Double-1>", display2)

root.mainloop()
