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

arr = io.imread("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_subset_big.tif")
print(arr.shape)

#data_list = [[[1, 2, 3], [4, 5,6 ,7, 8]],[[9, 10, 11, 12], [13, 14, 15, 16]]]
y = 1
x = 1

def prod_xy(x,y):
    return x, y

def parallel_runs(arr):
    pool = multiprocessing.Pool(processes=16)
    prod_x = partial(prod_xy, y) # prod_x has only one argument x (y is fixed to 10)
    result_list = pool.map(prod_x, arr)
   # print(result_list)
    string_arr = np.array_str(arr)
    f = open('chunk_array.txt','w')
    f.write(string_arr)
    f.close()

if __name__ == '__main__':
    parallel_runs(arr)
end_time = datetime.now()
print("end-time = ", end_time-start_time, "Hr:min:sec")