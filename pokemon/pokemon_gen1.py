import pandas as pd
import numpy as np
import random

print('hello world p')



data='pokedex.csv' # Select csv with pokemon info, set up to be in same folder as current file
#pokedex=pd.read_csv(data,index_col=0) # Import pokemon info and save as pokedex
pokedex=pd.read_csv(data,index_col=None) # No index in File, helps removing special evols, Import pokemon info and save as pokedex

#pokedex.rename(columns={"#":"Number"},inplace=True) # First time to change column name of "#"
#pokedex.rename(str.lower, axis='columns', inplace=True) # Changes column titles to lowercase, unsure if necissary


#pokedex.to_csv('pokedex.csv', index=True) # Saves file, 


# rand=random.randrange(0,len(pokedex))     #Random on all values
rand=random.randrange(0,151)                #151 pokemon in gen1
print(rand)
print("\n")
#print(pokedex.head(20))

## Need to Create a new pokedex to collect only all gen 1 Pokemon
## Only went to 151 pokemon, no special evolutions, 
## No other changes,technically didnt include fairy pokemon and other new types,
## So Fans would be upset, Science would be happy

for i in range (1,152): #looking at pokemon Numbers
    ii=0     #will be the previous pokemon Number
    if i != ii:
        print(pokedex.loc[i,"Name"])
        ii=i
    i+=i
   
    
    
    
    
    
    
