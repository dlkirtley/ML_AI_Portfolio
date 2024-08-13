import numpy
import matplotlib.pyplot as plt
from sklearn import datasets

data = datasets.fetch_california_housing(as_frame=True)
data = data.frame
print(data.head())

