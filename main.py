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

# Import Dataset from SkLearn
data = datasets.fetch_california_housing(as_frame = True)
data = data.frame
print(data.head())

# Visualize the Data

data.hist(bins=50, figsize=(24,24))

plt.figure(1)
attributes = ['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude','MedHouseVal']
scatter_matrix(data[attributes],figsize=(24,24))

plt.figure(2)
data.plot(kind="scatter", x="Longitude",y="Latitude", c="MedHouseVal", cmap="jet", colorbar=True, legend=True, sharex=False, figsize=(24,24), s=data['Population']/100, label="population", alpha=0.7)
plt.show()

