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
arr = io.imread("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_subset.tif")

#string_arr = np.array_str(arr)
#f = open('helloworld.txt','w')
#f.write(string_arr)
#f.close()

#Jonas-Laptop-Path:
#arr = io.imread("C:/Users/jz199/Desktop/S1A_VH_Agulhas_50m_selected_bands_VH_subset.tif")

####### Create Chunks ########

result_list = []

def mp_chunk(arr):
    chunks = [(sub_arr)
              for sub_arr in np.array_split(arr, mp.cpu_count())]

def parallel_runs(result_list):
    pool = multiprocessing.Pool(processes=16)
    #prod_x = partial(prod_xy, y=10) # prod_x has only one argument x (y is fixed to 10)
    result_list = pool.map(mp_chunk(arr), data_list)
    print(result_list)

if __name__ == '__main__':
    parallel_runs(data_list)

#print(len(chunks))
#print(chunks[15].shape)



end_time = datetime.now()
print("end-time = ", end_time-start_time, "Hr:min:sec")

if __name__ == '__main__':
    print(mp_chunk(arr))