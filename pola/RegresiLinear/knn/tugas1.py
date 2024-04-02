import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
from math import sqrt
import warnings
import os
warnings.filterwarnings('ignore')
print(os.getcwd())



def figure():
    data = pd.read_csv('d:\Python\LatihanPythonAmir\pola\RegresiLinear\knn\clustering.csv')
    print(data.head())
    global X
    X = data[["ApplicantIncome", 'LoanAmount']]

    #visualize data points
    plt.scatter(X["ApplicantIncome"],X["LoanAmount"],c='blue')
    plt.xlabel('ApplicantIncome')
    plt.ylabel('LoanAmount (In Thousands)')
    plt.show()
def titik_awal():
    data = pd.read_csv('d:\Python\LatihanPythonAmir\pola\RegresiLinear\knn\clustering.csv')
    X = data[["ApplicantIncome", 'LoanAmount']]
    K = 3
    # Select random observation as centroids
    global Centroids
    Centroids = (X.sample(n=K))
    plt.scatter(X["ApplicantIncome"],X["LoanAmount"],c='blue')
    plt.scatter(Centroids["ApplicantIncome"],Centroids["LoanAmount"],c='red')
    plt.xlabel('ApplicantIncome')
    plt.ylabel('LoanAmount (In Thousands)')
    plt.show()

    print(Centroids)
def hasil_clusterng():
    data = pd.read_csv('clustering.csv')
    X = data[["ApplicantIncome", 'LoanAmount']]
    K = 3

    # Select random observation as centroids
    Centroids = X.sample(n=K)
    #step 3 assign all the points to the closest cluster centroid
    #step 4 recompute centroids of newly formed clusters
    #step 5 repeat step 3 and 4

    diff = 1
    j=0

    while(diff!=0):
        # X = X.copy()  # Fix: Replace XD with X
        i=0
        for index1, row_c in Centroids.iterrows():
            ED=[]
            for index2, row_d in X.iterrows():  # Fix: Replace XD with X
                d1 = (row_c["ApplicantIncome"]- row_d["ApplicantIncome"])**2  # Fix: Correct the typo in "ApplicantIncome"
                d2 = (row_c["LoanAmount"]- row_d["LoanAmount"])**2
                d = sqrt(d1+d2)
                ED.append(d)
            X[i] = ED
            i = i+1

        C=[]
        for index, row in X.iterrows():
            min_dist=row[0]
            pos=0
            for i in range(K):
                if row[i] < min_dist:
                    min_dist = row[i]
                    pos=i
            C.append(pos)
        X["Cluster"]=C
        Centroids_new = X.groupby(["Cluster"]).mean()[["LoanAmount","ApplicantIncome"]]
        if j == 0:
            diff=1
            j = j+1
        else:
            diff = (Centroids_new['LoanAmount'] - Centroids['LoanAmount']).sum() + (Centroids_new['ApplicantIncome'] - Centroids['ApplicantIncome']).sum()
            print(diff.sum())
        Centroids = X.groupby(["Cluster"]).mean()[["LoanAmount","ApplicantIncome"]]

    #visualize data points
    color=['blue','green','cyan']
    for k in range(K):
        data=X[X["Cluster"]==k+1]
        plt.scatter(data["ApplicantIncome"],data["LoanAmount"],c=color[k])
    plt.scatter(Centroids["ApplicantIncome"],Centroids["LoanAmount"],c='red')
    plt.xlabel('Income')
    plt.ylabel('Loan Amount (In Thousands)')
    plt.show()
