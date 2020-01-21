from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly

filename = "C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_subset2.tif"

def gdal_array():
    #filename = 'C:/Users/jonas/Desktop/S1A_VH_Agulhas_50m_selected_bands_VH_subset.tif'
    #filename = "C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_subset2.tif"
    #filename = "C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VV_Agulhas_50m_selected_bands_VV.tif"
    ras = gdal.Open(filename, GA_ReadOnly)

    arr = ras.ReadAsArray()
    return(arr)


