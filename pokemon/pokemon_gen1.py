import pandas as pd
import os
from sklearn.model_selection import train_test_split
import time
from tqdm import tqdm

# import functions
from pokedex_generator import Gen1Pokedex
from image_manipulation import imageMaxPixel, rgbToArray
from SVM_Optimizer import SVM_kernal_Optim


# sprites is the location of sprite images for Gen1 pokemon
sprites = "C:\\Users\\brima\\Documents\\CodeProjectData\\PokemonSprites\\"\
    "pokemon\\main-sprites\\red-blue"


# create pokedex for gen1 pokemon
gen1 = Gen1Pokedex()


# create list of sprite file names and sprite file paths
spritenumber = []   # makes empty array for sprite file names
spritepath = []     # makes empty array for sprite file paths
for file in os.listdir(sprites):
    if file.endswith(".png"):
        spritenumber.append(os.path.splitext(file)[0])      # removes extension from sprite number
        spritepath.append(os.path.join(sprites, file))


# create a pd database with number and file location to sort
file_db = pd.DataFrame({"Number": spritenumber, "Path": spritepath, })      # create dataset
file_db = file_db.astype({'Number': 'int32'})    # column number was imported as an object, changes to int 32
file_db = file_db.sort_values(by='Number')      # sort by number
file_db = file_db.reset_index(drop=True)

# Find largst image pixel size
pixel = imageMaxPixel(spritepath)

# From Pixel size found, need to go in and resize each image
rgb_Array = rgbToArray(file_db, pixel) # creates array of the images rgb values flattened
file_db.insert(2, 'ImageArray', rgb_Array)  # add's image array to database

# Need to combine dataframes to have a list of pokemon numbers, name, type, and image array
Final_array = pd.merge(file_db, gen1, on='Number')

# Create a set of random pokemon to be the training set and test set
Image_train, Image_test, Type_train, Type_test = train_test_split(
    Final_array['ImageArray'], Final_array['Type'], test_size=0.8, random_state=42)

# For SVM testing
# Look for optimal kernal for multiple random statesd
values = []
i = 0
e = 100

pbar = tqdm(total=e)

for state in range(0, e, 1):
    Image_train, Image_test, Type_train, Type_test = train_test_split(Final_array['ImageArray'], Final_array['Type'], test_size=0.8, random_state=state)
    value = SVM_kernal_Optim(Image_train, Image_test, Type_train, Type_test, C=1)
    values.append(value)
    i += 1
    pbar.update(1)
print('Complete')

linear_perc = sum([i[0] for i in values])/e
rbf_perc = sum([i[1] for i in values])/e
poly_perc = sum([i[2] for i in values])/e

print('Running {} random data sets, a success rate of {:#.4g}% for linear,'\
      '{:#.4g}% for rbf, and {:#.4g}% for poly was found.'.format(e, linear_perc, rbf_perc, poly_perc))
