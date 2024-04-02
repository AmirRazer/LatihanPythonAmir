from tkinter import *
import pandas as pd
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt

root = Tk()
root.geometry("300x300")

OPTIONS = [
    "Option 1",
    "Option 2",
    "Option 3"
] 

def show_plot(selection):
    if selection == "Option 1":
        # Dataframe
        df = pd.DataFrame({'hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                           'score': [78, 79, 84, 80, 81, 89, 95, 90, 83, 89]})
        
        # Regplot
        p = sns.regplot(data=df, x='hours', y='score')
        
        # Calculate slope and intercept of regression equation
        slope, intercept, r, p_value, sterr = scipy.stats.linregress(x=p.get_lines()[0].get_xdata(),
                                                                     y=p.get_lines()[0].get_ydata())
        
        # Add regression equation to plot
        plt.text(2, 95, 'y = ' + str(round(intercept, 3)) + ' + ' + str(round(slope, 3)) + 'x')
        plt.title("Hours vs Scores")
        plt.show()

variable = StringVar()
variable.set(OPTIONS[0]) 

w = OptionMenu(root, variable, *OPTIONS, command=lambda selection: show_plot(selection))
w.pack()

root.mainloop()