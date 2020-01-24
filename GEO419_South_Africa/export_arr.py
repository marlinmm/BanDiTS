import rasterio as rio
from GEO419_South_Africa import import_arr

def out_array(outname, arr, input_file):
    with rio.open(input_file) as src:
        ras_data = src.read()
        ras_meta = src.profile

    # make any necessary changes to raster properties, e.g.:
    ras_meta['dtype'] = "float32"
    ras_meta['nodata'] = -99

    with rio.open(outname, 'w', **ras_meta) as dst:
        dst.write(arr, 1)