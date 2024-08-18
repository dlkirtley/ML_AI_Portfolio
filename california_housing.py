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

#Define X and Y Data. In this case it was chosen that this would be a single feature linear regression problem using median income.
medinc = Xtrain['MedInc']
medval = ytrain

combined = zip(medinc,medval)
combined_sort = sorted(combined, key = lambda x: x[0])
print(combined_sort)

print(f"{len(medinc)}-----{len(medval)}")

n = len(medinc)

sigmax = medinc.sum()
sigmay = medval.sum()

XY = np.array([])
XX = np.array([])
YY = np.array([])

for i in range(len(medinc)):
    XY=np.append(XY,medinc.iloc[i]*medval.iloc[i])
    XX = np.append(XX,medinc.iloc[i]**2)
    YY = np.append(YY,medval.iloc[i]**2)

sigmaXY = XY.sum()
sigmaXX = XX.sum()
sigmaYY = YY.sum()

a = ((sigmay*sigmaXX)-(sigmay*sigmaXY))/((n*sigmaXX)-sigmaXX)
b = ((n*sigmaXY)-(sigmax*sigmay))/((n*sigmaXX-sigmaXX))

yline = b*medinc+a
print(f"Y = {b}x+{a}")
plt.plot(medinc,yline,'r-')
plt.xlabel('MedInc')
plt.ylabel('MedHouseVal')
plt.title('Median House Value vs. Median Income')
plt.grid()
plt.scatter(medinc,medval, alpha = 0.2)
plt.show()









