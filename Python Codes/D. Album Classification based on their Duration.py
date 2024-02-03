import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as pt

data = pd.read_csv(r"C:\Users\Buland Jayeshkumar\OneDrive\Desktop\Spotify\spotify_taylorswift.csv")

albums_len = data.groupby(['album'])['length'].agg('sum')  # To Get Duration Of Each Album
d_al = dict(albums_len)

for j in d_al.keys():
    if d_al[j] == max(albums_len):
        print("MOST LONGEST ALBUM:", j)
    elif d_al[j] == min(albums_len):
        print("MOST SHORTEST ALBUM:", j)

"""
Output:
Python 3.10.0 (tags/v3.10.0:b494f59, Oct 4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32 Type "help", "copyright", "credits" or "license()" for more information.

﻿>>>
= RESTART: C:/Users/Buland Jayeshkumar/AppData/Local/Programs/Python/Python310/IP_AlbLength VS.py

MOST LONGEST ALBUM: Fearless (Taylor's Version) 
MOST SHORTEST ALBUM: Taylor Swift
>>>
"""
