import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import func


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

# func.guess_centroid(normdist_list, normspeed_list)

func.main(normdist_list, normspeed_list, ((-.5, .5), (-.5, 1.5), (2, 0), (2, 4), (1, 3)))
