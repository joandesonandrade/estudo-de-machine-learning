import pandas as pd
import numpy as np


data = pd.read_csv('dataset/normal_filmes.csv')

label = [dt for dt in data[0:1] if dt != "ID" and dt != 'Genre' and dt != 'Counter']

ndf = data.groupby(['Genre']).sum()

genre = data.groupby('Genre').size().reset_index()

dnp = np.array([ndf['audienceRating'], ndf['criticRating'], ndf['timeMin'], ndf['Year']])
qnp = np.array(ndf['Counter'])

media = dnp / qnp

genero = []
resultado = []

j = np.array(genre)

for i in j:
    genero.append(i[0])

for i in media:
    resultado.append(i)

final = pd.DataFrame(data=resultado, columns=genero, index=label)
final.to_csv('dataset/processado_filmes.csv')