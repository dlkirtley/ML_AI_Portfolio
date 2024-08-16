import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split as tts

#Import Data
data = datasets.fetch_california_housing(as_frame=True)
calihousing = data.frame

#Define Features and Targets
X = calihousing.drop('MedHouseVal',axis = 1)
y = calihousing['MedHouseVal']

#Split the data and visualize the data
Xtrain, Xtest, ytrain, ytest = tts(X,y,test_size = 0.2,random_state = 42)
#scatter_matrix (calihousing,alpha=0.2, figsize=(12,8),diagonal = 'kde')

#Investigate Correlation of features to target
correlation = calihousing.corr()
correlation = correlation['MedHouseVal'].sort_values(ascending=True)
print(correlation,"\n")

#Ensure Data is Complete
print(calihousing.isna().sum(),"\n")

#Ensure all Data is of the same type
print(calihousing.dtypes,"\n")

regression_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])
regression_pipeline.fit(Xtrain,ytrain)

ypred = regression_pipeline.predict(Xtest)
r2 = r2_score(ytest,ypred)

print(r2)





