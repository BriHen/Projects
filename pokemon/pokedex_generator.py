# -*- coding: utf-8 -*-

import pandas as pd
import random

def Gen1Pokedex():
    ## Need to Create a new pokedex to collect only all gen 1 Pokemon
    ## Only went to 151 pokemon, no special evolutions, 
    ## No other changes,technically didnt include fairy pokemon and other new types,
    ## So Fans would be upset, Science would be happy
    
    data='pokedex.csv' # Select csv with pokemon info, set up to be in same folder as current file
    #pokedex=pd.read_csv(data,index_col=0) # Import pokemon info and save as pokedex
    pokedex=pd.read_csv(data,index_col=None) # No index in File, helps removing special evols, Import pokemon info and save as pokedex
    
    #pokedex.rename(columns={"#":"Number"},inplace=True) # First time to change column name of "#"
    #pokedex.rename(str.lower, axis='columns', inplace=True) # Changes column titles to lowercase, unsure if necissary
    
    #pokedex.to_csv('pokedex.csv', index=True) # Saves file, 
       
    previous_pokemon=0      #assigns initial previous_pokemon Number
    gen1pokedex=pd.DataFrame({"Number":[],"Name":[],"Type":[]})       # Creates a blank pandas dataframe
    i=0         #assigns blank variable, to be used for the index values
    while previous_pokemon < 151 : #Stops when the last pokemon taken was number 151, mew
          pokemon_number=pokedex.loc[i,"Number"]    #Based on the index, selects the number
          pokemon_name=pokedex.loc[i,"Name"]        #Based on the index, selects the name
          pokemon_type=pokedex.loc[i,"Type 1"]      #Based on the index, selects the First type, which would be considered the main type
          if pokemon_number != previous_pokemon:    #To remove pokemon mega evolutions, only select the first time the pokemon appears in dataset
              current_pokemon=({"Number":[pokemon_number],"Name":[pokemon_name],"Type":[pokemon_type]}) #Creates a dict for the name number and type
              current_pokemon=pd.DataFrame(data=current_pokemon)    #Creates a dataframe for current pokemon, can be used for error checking
              gen1pokedex=gen1pokedex.append(current_pokemon)       #appends the current pokemon to the already building dataset
              #print(pokemon_number) #prints in console the pokemon number to see progression through dataset
              previous_pokemon=pokemon_number #saves previous pokemon label as data was already saved to database
              i+=1 #adds to the index value for next loop
          else:
              i+=1
    print('{} pokemon from Generation 1 saved, #{} {} was the final pokemon'.format(previous_pokemon,pokemon_number,pokemon_name))
    return gen1pokedex
