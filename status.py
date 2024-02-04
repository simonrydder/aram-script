import pandas as pd

champs = pd.read_csv('champs.csv')


print(champs['count'].sum())