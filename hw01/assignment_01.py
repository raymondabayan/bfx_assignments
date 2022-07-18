import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# os.listdir()
# names = pd.read_csv("peak_names_out.csv").head()
# counts = pd.read_csv("count_matrix.csv").head()

in_names = pd.read_csv("peak_names_out.csv", header = None, chunksize = 500)
in_names
in_counts = pd.read_csv("count_matrix.csv", chunksize = 2000)
chunk_list = []
for chunk in in_counts:
    chunk_list.append(chunk)

counts = pd.concat(chunk_list, ignore_index=True)
names = pd.concat(in_names, ignore_index=True)
data = pd.merge(names, counts, left_index= True, right_index= True)

clean_data = data.dropna(axis=0)
clean_data.rename(columns = {0 : "gene"}, inplace = True)

human = clean_data[clean_data["gene"].str.contains( "hg19_" )]
mouse = clean_data[clean_data["gene"].str.contains( "mm10_" )]

hcols = len(human.columns)

# df1 = human.melt(var_name = "columns", value_name = "values")
# df1
# df2 = pd.crosstab(index = df1['values'], columns = df1['columns'])
# df2
# human_counts = human.apply(pd.value_counts)
# human.apply(lambda x: x.value_counts())
# test = pd.concat([human[column].value_counts() for column in human], axis = 1)
# test = human.groupby(human.columns).size()
human_counts = []
for i in range(hcols):
    iter = human.iloc[:,i].value_counts()
    human_counts.append(iter)
    # pd.merge(human_counts, iter, left_index=True, right_index=True)
newdf = pd.DataFrame()
for col in range(hcols):
    iter = newdf.iloc[:, col].value_counts()
    newdf = newdf + iter

