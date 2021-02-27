# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 10:05:44 2021

@author: brima
"""

import cv2
import numpy as np

def imageMaxPixel(spritepath):
    pixel = 0         # create variable pixel to be used for resizeing
    for file in spritepath:
        im = cv2.imread(file)   # uses c2v to read image file
        if im.shape[1] > pixel:     # All sprites are square, take one of the dimensions to save the largest value
            pixel = im.shape[0]   # Save the largest value to pixel
        # print(im)              # Tester
    return pixel

def imageMinPixel(spritepath):
    pixel = 1000000000         # create variable pixel to be used for resizeing
    for file in spritepath:
        im = cv2.imread(file)   # uses c2v to read image file
        if im.shape[1] < pixel:     # All sprites are square, take one of the dimensions to save the largest value
            pixel = im.shape[0]   # Save the smallest value to pixel
        # print(im)              # Tester
    return pixel



def rgbToArray(db,pixel):
    rgb_temp = []
    for file in db['Path']:
        # print(file)
        im = cv2.imread(file)
        im = cv2.resize(im, (pixel, pixel), interpolation=cv2.INTER_LINEAR)
    #   using cv2, convert each image into the 3 channels, r, g, b
        r, g, b = cv2.split(im)     # seperates the three color channels, rgb
    #    r, g, b = cv2.split(cv2.imread(file))   # seperates the three color channels, rgb 
        b = np.asarray(b).reshape(-1)   # takes the multi dimensional array for the color and turns into one columnn
        g = np.asarray(g).reshape(-1)
        r = np.asarray(r).reshape(-1)
        rgb_array = np.concatenate((r, g, b))   # combines arrays together, making one large array with three colors
    #    file_db.loc[file_db.Path == file, ['ImageArray']] = rgb_array   #Looks through file_db and finds row based on the file path and changes the Image array value
        rgb_temp.append(rgb_array)  # Creates an array with all arrays of numbers to be combined later with database
    return rgb_temp







