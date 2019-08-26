import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('dataset/normal_filmes.csv')

#Críticas/Audiência
# x = np.array(data['criticRating'])
# y = np.array(data['audienceRating'])
# colors = np.random.rand(4583)
# area = 5
#
# plt.title("Gráfico de dispersão ~ Críticas/Audiência")
# plt.xlabel("Taxa de críticas")
# plt.ylabel("Taxa de Audiência")
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.show()

#Audiência/Tempo em minutos
# x = np.array(data['timeMin'])
# y = np.array(data['audienceRating'])
# colors = np.random.rand(4583)
# area = 5
#
# plt.title("Gráfico de dispersão ~ Tempo/Audiência")
# plt.xlabel("Tempo em minutos")
# plt.ylabel("Taxa de Audiência")
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.show()

#Utilizando pizza para demonstrar os dados processados
data = pd.read_csv('dataset/processado_filmes.csv')

labels = [dt for dt in data.columns if dt != 'ID']

sizes = []

ndf = np.array(data)

#TODO
# for q in range(3):
#     for j, i in enumerate(ndf[q]):
#         print(i)
#         sizes.append(i)

for j, i in enumerate(ndf[0]):
    if i != 'audienceRating':
        sizes.append(i)

explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.title('Taxa de audiência segmentação por gêneros 2000~2017')
plt.show()
