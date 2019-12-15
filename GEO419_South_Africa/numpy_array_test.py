"""
File to test numpy array and stuff like that
"""
import sys
import numpy
import os
from skimage import io
from datetime import datetime
import pathos.multiprocessing as mp

start_time = datetime.now()

numpy.set_printoptions(threshold=sys.maxsize)

#Marlin-PC-Path:
im = io.imread("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_subset.tif")

#Jonas-Laptop-Path:
#im = io.imread("C:/Users/jz199/Desktop/S1A_VH_Agulhas_50m_selected_bands_VH.tif")

shape = im.shape
print(shape)

result_list = []
time_list = []

def for_loop_pixel():
    for y in range(0, 122):
        for x in range(0,117):
            time_list = im[x, y, :]
            time_list = time_list[time_list != -99]
            result_list.append(time_list)
            x += 1
        y += 1
    print(result_list)
    mid_time = datetime.now()
    print("mid-time = ", mid_time - start_time, "Hr:min:sec")

for_loop_pixel()


print(shape)

mid_time = datetime.now()
print("mid-time = ", mid_time-start_time, "Hr:min:sec")