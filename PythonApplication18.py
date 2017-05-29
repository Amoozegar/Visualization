import pandas as pd
import numpy as np
data=pd.read_csv('baseball_data.csv')
del data['name']
del data['Handedness Abbreviation']

weight_bins = [0,160, 170, 180, 190, 200, 210, 220, 230]
weight_labels = [160, 170, 180, 190, 200, 210, 220, 230]
data['weight_bin'] = pd.cut(data['weight'], weight_bins, labels=weight_labels)
newBaseball = data.groupby(['weight_bin','handedness'], as_index=False).mean()
newBaseball.to_csv('New_baseball_data.csv')
print newBaseball