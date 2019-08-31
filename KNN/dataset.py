import pandas as pd


df = pd.read_csv('dataset/iris.csv')

print(df.groupby('variety').sum())