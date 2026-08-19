import tkinter as tk


def display1():
    print(l1.get(tk.ACTIVE))


def display2(w1):
    index = l1.curselection()[0]
    value = l1.get(index)
    print("selected item: ", value)


top = tk.Tk()
l1 = tk.Listbox(top)
l1.grid(row=1, column=1)
list1 = ["Java", "Python", "C++"]
for i in list1:
    l1.insert(tk.END, i)
b1 = tk.Button(top, text="Echo", width=10, command=display1)
b1.grid(row=1, column=2)
l1.bind("<<ListboxSelect>>", display2)
top.mainloop()
