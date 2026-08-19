import tkinter as tk


def display(event):
    s1 = E1.get()
    print(s1)


top = tk.Tk()
L1 = tk.Label(top, text="Password")
L1.pack(side=tk.LEFT)
E1 = tk.Entry(top, show="*")
E1.pack(side=tk.RIGHT)
E1.bind("<Return>", display)

top.title("first")
b1 = tk.Button(top, text="hello World", command=top.quit)
b1.pack(side=tk.BOTTOM)


top.geometry("1000x700")
top.mainloop()
