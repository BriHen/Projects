import pandas as pd
import numpy as np
import random
import glob2
import os
import cv2
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
file_db=pd.DataFrame({"Number":spritenumber,"Path":spritepath,}) # create dataset
file_db=file_db.astype({'Number':'int32'})  #column number was imported as an object, changes to int 32
file_db=file_db.sort_values(by='Number')    #sort by number
file_db=file_db.reset_index(drop=True)


## Need to go in and reshape images to be the size of the max sprite, and then flatten

## First find max size sprite, and save that as a variable to reshape all images
pixel=0         #create variable pixel to be used for resizeing
for file in spritepath:     
    im = cv2.imread(file)   # uses c2v to read image file
    if im.shape[1] > pixel: # All sprites are square, take one of the dimensions to save the largest value
        pixel=im.shape[0]   # Save the largest value to pixel
    #print(im)              # Tester


## From Pixel size found, need to go in and resize each image

rgb_temp=[]
for file in file_db['Path']:
    #print(file)
    im = cv2.imread(file)
    im = cv2.resize(im,(pixel,pixel),interpolation=cv2.INTER_LINEAR)    
## using cv2, convert each image into the 3 channels, r, g, b
    r, g, b = cv2.split(im)   # seperates the three color channels, rgb 
#    r, g, b = cv2.split(cv2.imread(file))   # seperates the three color channels, rgb 
    b = np.asarray(b).reshape(-1)   # takes the multi dimensional array for the color and turns into one columnn
    g = np.asarray(g).reshape(-1)
    r = np.asarray(r).reshape(-1)
    rgb_array=np.concatenate((r,g,b))   # combines arrays together, making one large array with three colors
#    file_db.loc[file_db.Path == file, ['ImageArray']] = rgb_array   #Looks through file_db and finds row based on the file path and changes the Image array value
    rgb_temp.append(rgb_array)  # Creates an array with all arrays of numbers to be combined later with database

file_db.insert(2,'ImageArray',rgb_temp) # add's image array to database

## Need to combine dataframes to have a list of pokemon numbers, name, type, and image array
Final_array=pd.merge(file_db, gen1, on = 'Number')

## For SVM create test array's of ImageArray and Type
# set Parameters for Training Set
trainSize=140;
trainImageArray=[]
trainTypeArray=[]

# set parameters for Testing Set
testImageArray=[]
testTypeArray=[]


trainImageArray=Final_array.loc[0:trainSize,'ImageArray'].tolist()
trainTypeArray=Final_array.loc[0:trainSize,'Type'].tolist()

testImageArray=Final_array.loc[trainSize:len(Final_array.index),'ImageArray'].tolist()
testTypeArray=Final_array.loc[trainSize:len(Final_array.index),'Type'].tolist()

#for i in range(trainSize,(len(Final_array.index))):
#    testImageArray.append(Final_array['ImageArray'][i])
#    testTypeArray.append(Final_array['Type'][i])
    
# For SVM testing
clf=svm.SVC()
clf.fit(trainImageArray,trainTypeArray)
for i in range(trainSize,len(Final_array.index)):
    predictionT = (clf.predict([Final_array.ImageArray[i]]))
    actualT = Final_array.Type[i]
    actualN = Final_array.Name[i]
    print(' {} Type Actual - {}; Predition - {};'.format(actualN,actualT, predictionT))
    
    
# Predict


## used to print an image on the screen to see size and resolution
cv2.imshow('image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

## 
#Final_array.loc[Final_array['ImageArray'] == i]
#resized = cv2.resize(imgage1, (im,im), interpolation=cv2.INTER_LINEAR)
    

    






