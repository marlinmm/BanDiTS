"""
File to test numpy array and stuff like that
"""
import sys
import numpy
import os
from skimage import io
from datetime import datetime
import pathos.multiprocessing as mp
import pylab as plt

start_time = datetime.now()

####### Print complete result array #########
numpy.set_printoptions(threshold=sys.maxsize)

####### Import Rasterstack #######
#Marlin-PC-Path:
im = io.imread("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_subset_big.tif")

#Jonas-Laptop-Path:
#im = io.imread("C:/Users/jz199/Desktop/S1A_VH_Agulhas_50m_selected_bands_VH_subset.tif")

####### Shape of Rasterstack ########
shape = im.shape
print("Raster-Stack-Shape = ", shape)

mid_time1 = datetime.now()
print("mid-time1 = ", mid_time1 - start_time, "Hr:min:sec")

####### Create empty result-lists #########
time_list = []
result_list = []

###### Iterate through Rasterstack #########
def for_loop_pixel():
    for y in range(0, 128):
        for x in range(0,58):
            time_list = im[x, y, :]

            #Eliminate -99 values
            time_list = time_list[time_list != -99]

            #tolist() makes it 10x faster
            result_list.append(time_list.tolist())
            x += 1
        y += 1
    print("Result-list = ", result_list)                        # Der erste Wert in der Liste ist komisch !!!
    print("Length of Result-list = ", len(result_list))
    #Test if every Result-list has 119 Time Series
    print(len(result_list[0]))
    print(len(result_list[2991]))

    #Plot for result_list[0]
    #plt.plot(result_list[0]) #if [x] in for(x)-Schleife, dann plottet der x*y Diagramme
    #plt.show()

    mid_time2 = datetime.now()
    print("mid-time2 = ", mid_time2 - start_time, "Hr:min:sec")

for_loop_pixel()

print("Raster-Stack-Shape = ", shape)
#print(shape)

#end_time = datetime.now()
#print("end-time = ", end_time-start_time, "Hr:min:sec")