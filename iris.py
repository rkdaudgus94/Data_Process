import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


iris =pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                  header= None,
                  names = ['sepal_length','sepal_width', 'petal_length', 'petal'])

print(iris.head())
print(iris.describe())