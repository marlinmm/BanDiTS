import rasterio
from matplotlib import pyplot
from rasterio.plot import *
import gdal
import matplotlib.pyplot as plt
import pylab as plt
from skimage import io
from datetime import datetime
#####################################################################################

start_time = datetime.now()

dataset = rasterio.open("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH.tif")
#dataset = rasterio.open("C:/Users/jz199/Desktop/S1A_VH_Agulhas_50m_selected_bands_VH.tif")

band_count = int(dataset.count)
print(band_count)


#for-Schleife für automatisierte Pixel-Iterating schreiben
ds = gdal.Open("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH.tif")
#ds = gdal.Open("C:/Users/jz199/Desktop/S1A_VH_Agulhas_50m_selected_bands_VH.tif")
myarray = np.array(ds.GetRasterBand(2).ReadAsArray())

value_list = []
value = 0
mid_time = datetime.now()
print("mid-time = ", mid_time-start_time, "Hr:min:sec")

# for-Schleife durch numpy.apply_along_axis() ersetzen, um nicht mehr durch alle Zeitreihen durchiterieren zu müssen
for band in range(1, band_count+1):
    myarray = np.array(ds.GetRasterBand(band).ReadAsArray())
    #mid2_time = datetime.now()
    #print("mid" + str(band) + "-time = ", mid2_time - start_time, "Hr:min:sec")
    value = float(myarray[500][500])
    value_list.append(value)
    band =+1
    #mide_time = datetime.now()
    #print("mid-end" + str(band) + "-time = ", mide_time - start_time, "Hr:min:sec")
mid3_time = datetime.now()
print("mid3-time = ", mid3_time-start_time, "Hr:min:sec")
# Unbrauchbare Werte eliminieren
value_list = np.array(value_list)
value_list = value_list[value_list != -99]


print(value_list)

end_time = datetime.now()
print("end-time = ", end_time-start_time, "hr:min:sec")

plt.plot(value_list)
plt.show()


