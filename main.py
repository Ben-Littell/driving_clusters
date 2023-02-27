import matplotlib.pyplot
import numpy as np
import pandas as pd

d_df = pd.read_csv('data.txt', delim_whitespace=True)
d_df.columns = ['id', 'dist', 'speed']


print(d_df)
