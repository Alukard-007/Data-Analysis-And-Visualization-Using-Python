import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv("C:\Users\Buland Jayeshkumar OneDrive\Desktop\Spotify\spotify_taylorswift.csv")

sns.set_style(style='darkgrid')
plt.figure(figsize=(10, 5))
plt.title('Top 5 Popular Songs')

top5 = data.sort_values('popularity', ascending=False).head(5)
sns.barplot(y='name', x='popularity', ci=None, palette='hls', data=top5)

plt.savefig(r"C:\Users\Buland Jayeshkumar OneDrive\Desktop\Viz_Images\Top5songs.png", transparent=True, bbox_inches='tight')
plt.show()
