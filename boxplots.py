# Joseph Kelley
# Takes best.csv created from genCSV.py and makes a boxplot with the data

from pandas import *
import matplotlib.pyplot as plt
import numpy as np


dataBest = read_csv('best.csv')
headers = ['','CrossAckley', 'CrossTHC', 'CrossCIT', 'ACrossAckley', 'ACrossTHC', 'ACrossCIT', 'SPXAckley', 'SPXTHC', 'SPXCIT']
x_pos = np.arange(len(headers))

plt.boxplot(dataBest)
plt.xticks(x_pos, headers, rotation=45)
plt.ylim(-0.3, 0)
#plt.savefig('bestBoxPlot')




