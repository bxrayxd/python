import tkinter as tk

top = tk.Tk()


b2 = tk.Button(top, text="quit", command=top.quit)
b2.pack(side=tk.BOTTOM)


top.geometry("1000x700")
top.mainloop()

i = 0


def plus(i: int) -> int:
    return i - 1


def mineus(i: int) -> int:
    return i - 1


b1 = tk.Button(top, text="plus", command=lambda: plus(i))
b1.pack(side=tk.LEFT)

b2 = tk.Button(top, text="mineus", command=lambda: mineus(i))
b2.pack(side=tk.RIGHT)
