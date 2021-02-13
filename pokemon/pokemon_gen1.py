import pandas as pd
import numpy as np
import random
import glob2
import os

# import functions
from pokedex_generator import Gen1Pokedex

#sprites is the location of sprite images for Gen1 pokemon
sprites= "C:\\Users\\brima\\Documents\\CodeProjectData\\PokemonSprites\\pokemon\\main-sprites\\red-blue"

#create pokedex for gen1 pokemon
gen1=Gen1Pokedex()

#create list of sprite file names and sprite file paths
spritename=[] # makes empty array for sprite file names
spritepath=[]   #makes empty array for sprite file paths
for file in os.listdir(sprites):
    if file.endswith(".png"):
        spritename.append(file)
        spritepath.append(os.path.join(sprites,file))





