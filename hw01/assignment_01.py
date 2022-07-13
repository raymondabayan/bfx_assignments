import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# os.listdir()
# names = pd.read_csv("peak_names_out.csv").head()
# counts = pd.read_csv("count_matrix.csv").head()

in_names = pd.read_csv("peak_names_out.csv", header = None, chunksize = 500)
in_counts = pd.read_csv("count_matrix.csv", chunksize = 500)
counts = pd.concat(in_counts, ignore_index=True)
names = pd.concat(in_names, ignore_index=True)
data = pd.merge(names, counts, left_index = True, right_index = True)

has1 = data.iloc[:, 1:-1] == 1
data[has1]
hasmore = data.iloc[:, 0] >= 2
more_than1 = data[hasmore]

plt.scatter(more_than1.index, more_than1[:, 0])
plt.show()

# iterate through each row to get the total number of droplets with
# 1 transcript
has_1 = pd.DataFrame()
for row in data.index:
    has_1.append(data[data.iloc[row, :] == 1])
    row += 1 


