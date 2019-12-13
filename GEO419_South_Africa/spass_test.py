import rasterio
from matplotlib import pyplot
from rasterio.plot import *
import gdal
import matplotlib.pyplot as plt
import pylab as plt

dataset = rasterio.open("C:/Users/jonas/Desktop/SubsetVH.tif")

band_count = int(dataset.count)
print(band_count)

ds = gdal.Open("C:/Users/jonas/Desktop/SubsetVH.tif")
myarray = np.array(ds.GetRasterBand(1).ReadAsArray())

value_list = []
value = 0

for band in range(1, band_count+1):
    myarray = np.array(ds.GetRasterBand(band).ReadAsArray())
    value = float(myarray[500][500])
    value_list.append(value)
    band =+1

value_list = np.array(value_list)
value_list = value_list[value_list != -99]

print(value_list)

plt.plot(value_list)
plt.show()
