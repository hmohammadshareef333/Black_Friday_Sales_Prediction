import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("https://raw.githubusercontent.com/nanthasnk/Black-Friday-Sales-Prediction/master/Data/BlackFridaySales.csv")
data.head()
data.shape
data.info()
data.isnull().sum()
data.isnull().sum()/data.shape[0]*100
data.nunique()