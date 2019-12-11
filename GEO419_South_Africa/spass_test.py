import rasterio
from matplotlib import pyplot
from rasterio.plot import *
import gdal
import matplotlib.pyplot as plt
import pylab as plt

dataset = rasterio.open("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH.tif")

band_count = int(dataset.count)
print(band_count)

ds = gdal.Open("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH.tif")
myarray = np.array(ds.GetRasterBand(3).ReadAsArray())

value_list = []
value = 0
for band in range(1, band_count+1):
    myarray = np.array(ds.GetRasterBand(band).ReadAsArray())
    value = float(myarray[1000][1000])
    value_list.append(value)
    band =+1
print(value_list)
plt.plot(value_list)
plt.show()
