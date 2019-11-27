#test3eteatda

# add shit 2

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:54:54 2019

@author: jonas
"""


import matplotlib.pyplot as plt
import pylab as plt
import numpy as np
import pandas as pd
import skimage
import skimage.filters as filters
from skimage import io
from skimage.io import imread
from skimage.segmentation import felzenszwalb, mark_boundaries

"""
df = pd.read_csv("C:/Users/jonas/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/Ziemer_uebungen/Python/data/testpivot3EEVH.csv")

print(df.head())

print(df.tail())

x = df['Band']
y = df['VH']
plt.xlabel('Time Series'); plt.ylabel('VH')
plt.plot(x,y)

"""

id = 0

filenames = ["VH"]

filename = "C:/Users/marli/Desktop/GEO402_Testdaten/test_1d_" + filenames[id] + ".tif"


img = imread(filename)


#plt.plot(img)

plt.imshow(img)
plt.show()
"""
I = plt.imread("C:/Users/jonas/Desktop/Subset_VV.tif")
"""

# Parameters to twiggle
scale = 1000   # Higher means larger clusters
sigma = 0.5   # Smoothing parameter for Gaussian kernel prior segmentation
min_size = 50 # minimum component size (enforced during processing)

segments_fz = felzenszwalb(img, scale=scale, sigma=sigma, min_size=min_size)

print("Felzenszwalb number of segments: {}".format(len(np.unique(segments_fz))))

plt.imshow(mark_boundaries(img, segments_fz))
plt.show()
