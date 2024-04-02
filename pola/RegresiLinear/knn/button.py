import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import semua fungsi dari file tugas1
from tugas1 import *


root = tk.Tk()

loan_button = tk.Button(root, text="Figure Peminjam", command=figure)
loan_button.pack()

centroid_button = tk.Button(root, text="Figure Titik awal centroid", command=titik_awal)
centroid_button.pack()

clustering_button = tk.Button(root, text="Hasil Clustering", command=hasil_clusterng)
clustering_button.pack()

root.mainloop()