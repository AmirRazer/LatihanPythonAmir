from tkinter import *
root = Tk()
root.geometry("300x300")

OPTIONS = [
    "LinerRegresi",
    "KNN"
]

Variable = StringVar()
Variable.set(OPTIONS[0])

w = OptionMenu(root, Variable, *OPTIONS)
w.pack()
root.mainloop()