import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as pt

data = pd.read_csv(r"C:\Users\Buland Jayesh kumar\OneDrive\Desktop\Spotify\spotify_taylorswift.csv")

ax = pt.axes()
pos = ['bottom', 'left']
ax.spines[pos].set_color('violet')
ax.spines[pos].set_linewidth(2)
ax.tick_params(axis='x', colors='violet')
ax.tick_params(axis='y', colors='violet')

sns.violinplot(x=data['acousticness'], y=data['album'], inner=None, color='blue')
sns.violinplot(x=data['energy'], y=data['album'], inner=None, color='red')
sns.violinplot(x=data['danceability'], y=data['album'], inner=None, color='green')

pt.savefig("C:\Users\Buland Jayeshkumar\OneDrive\Desktop\Viz_Images\AlbumStats.png", transparent=True, bbox_inches='tight')
pt.show()
