import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Buland Jayeshkumar OneDrive\Desktop\Spotify\spotify_taylorswift.csv")

alb_scount = data.groupby(['album']).size()
alb_scd = dict(alb_scount)
albums = list(alb_scd.keys())
alb_scount = list(alb_scount)
albums_pop = []  # To Contain Popularity of Each Album

for i in albums:
    alb_psum = data.loc[data['album'] == i, 'popularity'].sum()  # Summation of Popularity of Each Album
    albums_pop.append(alb_psum)

poppercent = []

for j in range(9):
    maxpop = 100 * alb_scount[j]
    alb_percent = (((albums_pop[j]) / maxpop) * 100)
    alb_percent = alb_percent.round(2)
    poppercent.append(alb_percent)

plt.pie(
    poppercent,
    labels=albums,
    startangle=90,
    shadow=False,
    explode=(0, 0, 0.1, 0, 0, 0, 0, 0, 0),
    radius=1.2,
    autopct='% 1.1f%%',
    pctdistance=0.8
)

# Giving a Donut Shaped View to Pie-Chart
centre_circle = plt.Circle((0, 0), 0.70, fc='black')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# plt.legend()
plt.savefig("C:\Users\Buland Jayeshkumar OneDrive\Desktop\Spotify\Viz_Images\New folder\Album Pie.png", transparent=True, bbox_inches='tight')
plt.show()
