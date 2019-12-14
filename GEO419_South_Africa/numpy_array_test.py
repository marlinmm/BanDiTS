"""
File to test numpy array and stuff like that
"""
import sys
import numpy
import os
from glob import glob
import matplotlib.pyplot as plt
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
from skimage import io
from datetime import datetime

start_time = datetime.now()

numpy.set_printoptions(threshold=sys.maxsize)
im = io.imread("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_subset.tif")
print(im.shape)
result_list = []
time_list = []

for y in range(0, 122):
    for x in range(0,117):
        time_list = im[x, y, :]
        time_list = time_list[time_list != -99]
        result_list.append(time_list)
        x += 1
    y += 1


print(time_list)
print(result_list)

mid_time = datetime.now()
print("mid-time = ", mid_time-start_time, "Hr:min:sec")