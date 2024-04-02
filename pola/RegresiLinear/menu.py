from tkinter import *
root = Tk()
from regresinew import regres
root.geometry("300x300")

OPTIONS = [
    "LinerRegresi",
    "KNN"
]

Variable = StringVar()
Variable.set(OPTIONS[0])

w = OptionMenu(root, Variable, *OPTIONS, command=lambda selection: regres(selection))
#buatkan perintah untuk memangil fungsi regres yang ada di regresnew

w.pack()
root.mainloop()