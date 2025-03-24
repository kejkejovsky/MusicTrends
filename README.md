# MusicTrends
Project aims to present changes in song durations over past years.
For this purpose, it uses a dataset of 30,000 songs from Spotify from the period 1957-2020.
The main script extracts the data from the file, transforms it and load it to the database.
The visualization script is responsible for presenting a simple plot comparing the mean length of songs over the years.
The detailed analysis is done in a jupyter notebook.

# Technology
- Python
- postgresql

# Data
https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs

# Simple result
![Alt text](/SongDuration.png?raw=true "Songs duration over years")

# Extended analysis
[a relative link](notebooks/Analysis.pdf)
Extended analysis presents change of song durations over years, divided by genres and histogram of change over decades.