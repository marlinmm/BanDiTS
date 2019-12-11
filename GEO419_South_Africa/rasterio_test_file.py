import rasterio
from matplotlib import pyplot
from rasterio.plot import *


dataset = rasterio.open("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH.tif")

print(dataset.count)

for i in range(0,dataset.count-2):
    print(i)
    i+=1

show(dataset, 1)

show(dataset, 3)


#print(dataset.name)
#print(dataset.bounds)

#pyplot.imshow(dataset.read(1), cmap='binary')
#pyplot.show()

#show_hist(dataset, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram")
#pyplot.show()