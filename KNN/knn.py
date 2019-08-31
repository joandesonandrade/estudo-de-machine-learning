import pandas as pd
import numpy as np
import math
from sklearn.model_selection import train_test_split

df = pd.read_csv('dataset/iris.csv')

ndf = np.array(df)

def euclidiana(vetor, x):
    v1 = [i for i in vetor if not str(i).isalnum()]
    v2 = [i for i in x if not str(i).isalnum()]
    while len(v1) != len(v2):
        if len(v1) > len(v2):
            v1.append(0)
        else:
            v2.append(0)
    nv1 = np.array(v1)
    nv2 = np.array(v2)
    dif = nv1 - nv2
    dist = np.dot(dif, dif)
    return math.sqrt(dist)

data_train, data_test, target_train, target_test = \
train_test_split(df, df, test_size=0.25, random_state=0)

row = np.array(data_test)[0]
train = np.array(data_train)

distances = np.fromiter((euclidiana(row, x) for x in train), np.float)

rank = distances.argsort()
best_ranks = rank[:10]

h = []
c = ['a', 'b', 'c', 'd', 'e']
for j in best_ranks:
    h.append(train[j])

h = pd.DataFrame(h, columns=c)
h = np.array(h['e'].value_counts().index.tolist())
result = h[0]

print('Entrada:', row[4])
print('Resultado:', result)

if result == row[4]:
    print('Acertou!!!')