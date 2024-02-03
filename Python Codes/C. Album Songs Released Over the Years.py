import pandas as pd
from matplotlib import pyplot as pt

data = pd.read_csv(r"C:\Users\Buland Jayeshkumar OneDrive\Desktop\Spotify\spotify_taylorswift.csv")
data.release_date = pd.to_datetime(data.release_date)  # Changing Date Format

years = data.release_date.dt.year  # Extract Only Years
years_unique = []  # To Take Unique Year Values

for i in years:
    if i not in years_unique:
        years_unique.append(i)

song_count = []

for i in years_unique:
    cont = 0
    for j in years:
        if i == j:
            cont += 1
    song_count.append(cont)

ax = pt.axes()
pos = ['bottom', 'left']
ax.spines[pos].set_color('darkblue')
ax.spines[pos].set_linewidth(3)
ax.tick_params(axis='x', colors='darkblue')
ax.tick_params(axis='y', colors='darkblue')

pt.title('Frequency of Album Songs Released Over The Years')
pt.xlabel('Years')
pt.ylabel('Number of Songs')
pt.plot(years_unique, song_count, 'g', linewidth=5, marker='o', markerfacecolor='blue', markersize=10)

pt.savefig("C:\Users\Buland Jayeshkumar OneDrive\Desktop\Viz_Images\SongReleases.png", transparent=True, bbox_inches='tight')
pt.show()
