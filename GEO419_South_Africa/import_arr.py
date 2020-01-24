from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly


def gdal_array(input_file):
    ras = gdal.Open(input_file, GA_ReadOnly)
    arr = ras.ReadAsArray()
    return(arr)


