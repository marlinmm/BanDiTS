import rasterio as rio
from GEO419_South_Africa import import_arr

def out_array():
    with rio.open(import_arr.filename) as src:
        ras_data = src.read()
        ras_meta = src.profile

    # make any necessary changes to raster properties, e.g.:
    ras_meta['dtype'] = "float32"
    ras_meta['nodata'] = -99

    with rio.open("C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/test1.tif", 'w', **ras_meta) as dst:
        dst.write(numpy_array, 1)