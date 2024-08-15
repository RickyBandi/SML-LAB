import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
from scipy.stats import skew
from scipy.stats import kurtosis
from scipy.stats import iqr
data=pd.read_csv('/content/drive/MyDrive/heart_attack_dataset.csv',usecols=(['Age']))
#data.tail(-1)
#print(data)
p=data.head(20)
print(data.head(20))
#plt.hist(data,100)
print("The Mean of the data=",np.mean(data))
print("The Median of the data=",np.median(data))
print("The Mode of the data=",stat.mode(data))
print("The SD of the data=",np.std(data))
print("The Skew of the data=",skew(data,axis=0,bias=True))
print("The kurtosis of the data=",kurtosis(data,axis=0,bias=True))
print("The IQR of the data=",iqr(data))
print("B.Rithwik 2303A52330")
print("Batch - 35")