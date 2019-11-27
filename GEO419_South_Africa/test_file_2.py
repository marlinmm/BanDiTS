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
from PIL import Image


"""
df = pd.read_csv("C:/Users/jonas/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/Ziemer_uebungen/Python/data/testpivot3EEVH.csv")

print(df.head())

print(df.tail())

x = df['Band']
y = df['VH']
plt.xlabel('Time Series'); plt.ylabel('VH')
plt.plot(x,y)

"""

id = 1

filenames = ["VH", "VV"]

filename = "C:/Users/jonas/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/Ziemer_uebungen/Python/data/radar/Subset_" + filenames[id] + ".tif"


img = skimage.io.imread(filename)


plt.plot(img)

"""
I = plt.imread("C:/Users/jonas/Desktop/Subset_VV.tif")
"""