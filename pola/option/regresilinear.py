import pandas as pd
import scipy
import seaborn as sns
import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression

df = pd.DataFrame({'hours':[1,2,3,4,5,6,7,8,9,10],
                   'score':[78,79,84,80,81,89,95,90,83,89]})
print(df)
p = sns.regplot(data=df,x=df.hours,y=df.score)
slope, intercept,r,p,sterr = scipy.stats.linregress(x=p.get_lines()[0].get_xdata(),
                                                     y=p.get_lines()[0].get_ydata())
#hitung berapa nilai regresnya



plt.text(2,95,'y = ' + str(round(intercept,3)) + '+' + str(round(slope,3))+ 'x')
plt.title("Hourse Vs Score")
plt.show()