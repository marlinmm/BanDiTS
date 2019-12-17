import sys
import os
from datetime import datetime
import numpy as np
import pathos.multiprocessing as mp
from pathos import multiprocessing
from multiprocessing import Process
from skimage import io
import pylab as plt

start_time = datetime.now()

####### Print complete result array #########
np.set_printoptions(threshold=sys.maxsize)

####### Import Rasterstack #######
#Marlin-PC-Path:
#im = io.imread("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_subset.tif")

#Jonas-Laptop-Path:
arr = io.imread("C:/Users/jz199/Desktop/S1A_VH_Agulhas_50m_selected_bands_VH_subset.tif")

####### Create Chunks ########
chunks = [(sub_arr)
          for sub_arr in np.array_split(arr, mp.cpu_count())]

####### Create empty result-lists #########
time_list = []
result_list = []

###### Iterate through Rasterstack #########
def for_loop_pixel():
    for y in range(0, 88):
        for x in range(0, 34):
            time_list = arr[x, y, :]

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

    #1st attempt with Pool-Processing - does not work very well
    # dont run that itll kill your cpu !!!
    pool = multiprocessing.Pool(mp.cpu_count())
    results = pool.map(for_loop_pixel, chunks)  # needs to be placed at the right position in script
    # Freeing the workers:
    pool.close()
    pool.join()

    #2nd attempt with Processing - does even bigger shit then 1st attempt
    #for i in range(len(chunks)):
    #    pool = Process(target=for_loop_pixel(), args=(chunks[i],))
    #    pool.start()
    #    pool.join()

for_loop_pixel()

# Individuell nach Anzahl logischer Prozessoren (-1) angeben
print(len(chunks))
print(chunks[11].shape)

print(sum([chunk.shape[0] for chunk in chunks]))