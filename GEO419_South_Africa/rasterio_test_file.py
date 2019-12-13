import rasterio
from matplotlib import pyplot
from rasterio.plot import *
from osgeo import gdal
"""
dataset = rasterio.open("C:/Users/jonas/Desktop/PivotVH4.tif")

print(dataset.count)

for i in range(0,dataset.count-2):
    print(i)
    i+=1

show(dataset, 1)

show(dataset, 3)
"""

ds = gdal.Open("C:/Users/jonas/Desktop/test_1d_VH.tif")
myarray = np.array(ds.GetRasterBand(1).ReadAsArray())
print(myarray)

#print(dataset.name)
#print(dataset.bounds)

#pyplot.imshow(dataset.read(1), cmap='binary')
#pyplot.show()

#show_hist(dataset, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram")
#pyplot.show()