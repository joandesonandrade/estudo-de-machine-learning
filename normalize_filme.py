import pandas as pd
import numpy as np

dataFrame = pd.read_csv('dataset/filmes.csv')

lista_audienceRating = [dt for dt in dataFrame['audienceRating']]
lista_Genre = [dt for dt in dataFrame['Genre']]
lista_criticRating = [dt for dt in dataFrame['criticRating']]
lista_timeMin = [dt for dt in dataFrame['timeMin']]
lista_Year = [dt for dt in dataFrame['Year']]

data = []
columns = ['audienceRating', 'Genre', 'criticRating', 'timeMin', 'Year', 'Counter']

for i in range(len(lista_audienceRating)):
    data.append([lista_audienceRating[i], lista_Genre[i], lista_criticRating[i], lista_timeMin[i], lista_Year[i], 1])

n = pd.DataFrame(data=np.array(data), columns=columns)
n.to_csv("dataset/normal_filmes.csv")