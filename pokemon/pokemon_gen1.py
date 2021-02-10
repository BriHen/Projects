import pandas as pd
import numpy as np
import random

print('hello world p')



data='pokedex.csv'
pokedex=pd.read_csv(data,index_col=0)
#pokedex.rename(columns={"#":"Number"},inplace=True) # First time to change column name of "#"
#pokedex.rename(str.lower, axis='columns', inplace=True)


pokedex.to_csv('pokedex.csv', index=True)
# rand=random.randrange(0,len(pokedex))     #Random on all values
rand=random.randrange(0,151)                #151 pokemon in gen1
print(rand)
print(pokedex.iloc[rand])
print('Last - 151')
print(pokedex.loc[6])
print(pokedex.head(20))
