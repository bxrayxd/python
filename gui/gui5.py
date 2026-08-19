import tkinter as tk


win = tk.Tk()


def display(i):
    if i == 0:
        print("you win")
    else:
        print("you lose")


def more(i) -> int:
    i = +1
    return i


win.title("hi")

b1 = tk.Button(win, text="you win", command=lambda: display(0))
b1.pack(side=tk.LEFT)


b2 = tk.Button(win, text="quit", command=win.quit)
b2.pack(side=tk.BOTTOM)


win.geometry("1000x700")
win.mainloop()
