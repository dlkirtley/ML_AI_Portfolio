## Import packages, Libraries, and Modules
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import sys


def data_vis(data):
    # Visualize the Data as a Histogram
    data.hist(bins=50, figsize=(12,8))

    # Viusalize the Data by comparing features to each other and look for trends
    plt.figure(1)
    attributes = list(data.columns)
    scatter_matrix(data[attributes],figsize=(12,8))
    plt.show()

def validate(data):
    print(data.dtypes, data.isna().sum())

def split_data(data,target):
    #X = data[['HouseAge','AveRooms','MedInc']]
    X = data.drop(target,axis = 1)
    y = data[target]

    return X, y

def correlation_check(data):
    corr = data.corr()
    target_corr = corr[target[0]].sort_values(ascending = True)
    print(target_corr)

    return target_corr

def training(X,y):
    Xtrain, Xtest,ytrain,ytest = tts(X,y,test_size=0.01,random_state=42)

    return Xtrain,Xtest,ytrain,ytest

def mod_select():
    model_selection = int(input("\nPlease enter the number of the model you would like to choose:\n 1) Linear Regression\n 2) Random Forest\n"))
    if model_selection == 1:
        model = LinearRegression()
    return model

# Import Dataset from SkLearn and define the target
data = datasets.fetch_california_housing(as_frame = True)
print(data.DESCR)
data = data.frame
print(data.head())
target =['MedHouseVal']
proceed = input(f"Target set as {target}. Do you want to Proceed (Y/n)?")

if proceed == "Y":
    

    # Call Functions
    #plots = data_vis(data)
    validation = validate(data)
    target_corr = correlation_check(data)
    X,y = split_data(data,target)
    Xtrain,Xtest,ytrain,ytest = training(X,y)
    model = mod_select()
    model.fit(Xtrain,ytrain)
    ypred = model.predict(Xtest)
    r2 = r2_score(ypred,ytest)
    print(f"R2 Score: {r2}")
    mse = mean_squared_error(ypred,ytest)
    print(f"Mean Squared Error: {mse}")
    plt.scatter(ypred,ytest)
    plt.xlabel('Predicted Value')
    plt.ylabel('Actual Value')
    plt.grid()
    plt.show()
    
else:
    print('Terminating Runtime Instance')
    sys.exit()
