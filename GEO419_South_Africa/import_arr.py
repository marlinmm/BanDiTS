from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly

#filename = "C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_minisubset3456.tif"


#filename = "C:/Users/jz199/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_minisubset3456.tif"
#filename = "C:/Users/jz199/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_subset_big.tif"
filename = "C:/Users/jz199/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_subset2.tif"

def gdal_array():
    ras = gdal.Open(filename, GA_ReadOnly)
    arr = ras.ReadAsArray()
    return(arr)


