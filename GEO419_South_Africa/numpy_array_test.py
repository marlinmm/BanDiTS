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
im = io.imread("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH.tif")
print(im.shape)

test_list = im[1, 2, :]
test_list = test_list[test_list != -99]
mid_time = datetime.now()


plt.plot(test_list)
plt.show()
print("mid-time = ", mid_time-start_time, "Hr:min:sec")
print(type(im))
