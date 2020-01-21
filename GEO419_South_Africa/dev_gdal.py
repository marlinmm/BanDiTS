from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly

filename = 'C:/Users/jonas/Desktop/S1A_VH_Agulhas_50m_selected_bands_VH_subset.tif'

ras = gdal.Open(filename, GA_ReadOnly)

arr = ras.ReadAsArray()
