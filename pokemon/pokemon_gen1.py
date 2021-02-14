import pandas as pd
import numpy as np
import random
import glob2
import os
from sklearn import svm
import imageio
from PIL import Image

# import functions
from pokedex_generator import Gen1Pokedex

#sprites is the location of sprite images for Gen1 pokemon
sprites= "C:\\Users\\brima\\Documents\\CodeProjectData\\PokemonSprites\\pokemon\\main-sprites\\red-blue"

#create pokedex for gen1 pokemon
gen1=Gen1Pokedex()


#create list of sprite file names and sprite file paths
spritenumber=[] # makes empty array for sprite file names
spritepath=[]   #makes empty array for sprite file paths
for file in os.listdir(sprites):
    if file.endswith(".png"):
        spritenumber.append(os.path.splitext(file)[0]) # removes extension from sprite number
        spritepath.append(os.path.join(sprites,file))

## create a pd database with number and file location to sort
file_db=pd.DataFrame({"Number":spritenumber,"Path":spritepath}) # create dataset
file_db=file_db.astype({'Number':'int32'})  #column number was imported as an object, changes to int 32
file_db=file_db.sort_values(by='Number')    #sort by number


## Need to go in and reshape images to be the size of the max sprite, and then flatten




## First find max size sprite, and save that as a variable to reshape all images
maxpixel=0
for file in spritepath:
    im = imageio.imread(file)
    if im.shape[1] > maxpixel:
        maxpixel=im.shape[0]
    print(im)
    

    






