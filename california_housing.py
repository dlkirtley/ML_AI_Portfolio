import numpy
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split as tts


data = datasets.fetch_california_housing(as_frame=True)
calihousing = data.frame

X = calihousing.drop('MedHouseVal',axis = 1)
y = calihousing['MedHouseVal']

Xtrain, Xtest, ytrain, ytest = tts(X,y,test_size = 0.2,random_state = 42)
scatter_matrix (calihousing,alpha=0.2, figsize=(12,8),diagonal = 'kde')
plt.show()
print(X.head())



