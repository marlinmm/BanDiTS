"""
File to test numpy array and stuff like that
"""
import os
from glob import glob
import matplotlib.pyplot as plt
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
from skimage import io

im = io.imread("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH.tif")
print(im.shape)

print(type(im))

print(im)