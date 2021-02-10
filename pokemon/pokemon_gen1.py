import pandas as pd
import numpy as np
import random

print('hello world p')



data='Pokemon.csv'
pokedex=pd.read_csv(data,index_col=0)

rand=random.randrange(0,len(pokedex))
print(rand)
print(pokedex.iloc[rand])
