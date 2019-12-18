import sys
import os
from datetime import datetime
import numpy as np
import pathos.multiprocessing as mp
from pathos import multiprocessing
from multiprocessing import Process
from skimage import io
import pylab as plt
import multiprocessing
from functools import partial

np.set_printoptions(threshold=sys.maxsize)
start_time = datetime.now()

####### Import Rasterstack #######
#Marlin-PC-Path:
#arr = io.imread("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_subset.tif")

#Jonas-Laptop-Path:
arr = io.imread("C:/Users/jz199/Desktop/Pivot_subset.tif")
#list_arr = list(arr)
#arr = io.imread("C:/Users/jonas/Desktop/S1A_VH_Agulhas_50m_selected_bands_VH_subset_big.tif")

print(arr.shape)

####### Create Chunks ########
#chunks = [(sub_arr)
#          for sub_arr in np.array_split(arr, mp.cpu_count())]

#data_list = [[[1, 2, 3], [4, 5,6 ,7, 8]],[[9, 10, 11, 12], [13, 14, 15, 16]]]
y = 1
x = 1

def prod_xy(x,y):
    return x,y

def parallel_runs():
    pool = multiprocessing.Pool(processes=1)
    prod_x = partial(prod_xy, y) # prod_x has only one argument x (y is fixed to 10)
    result_list = pool.map(prod_x, arr)
    print(result_list)
    string_arr = np.array_str(arr)
    f = open('chunk_array.txt','w')
    f.write(string_arr)
    f.close()
    #pool.close()
    #pool.join()

if __name__ == '__main__':
    parallel_runs()

end_time = datetime.now()
print("end-time = ", end_time-start_time, "Hr:min:sec")