import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def guess_centroid(list1, list2):
    plt.scatter(list1, list2)
    plt.show()
    guess = input('Input Centroid Locations: ')
    guess = eval(guess)  # if written as coordinate points gives tuple or tuple of tuples
    # print(type(guess[0][1]))
    return guess


# change column names
d_df = pd.read_csv('data.txt', delim_whitespace=True)
d_df.columns = ['id', 'dist', 'speed']
# print(d_df)
## initial visualisation

dist_list = d_df['dist'].values.tolist()
speed_list = d_df['speed'].values.tolist()

# plt.scatter(dist_list, speed_list)
# plt.show()

d_df['norm dist'] = (d_df.dist - d_df.dist.mean())/d_df.dist.std()
d_df['norm speed'] = (d_df.speed - d_df.speed.mean())/d_df.speed.std()

normdist_list = d_df['norm dist'].values.tolist()
normspeed_list = d_df['norm speed'].values.tolist()

# print(d_df['norm speed'])
# plt.scatter(normdist_list, normspeed_list)
# plt.show()

guess_centroid(normdist_list, normspeed_list)

