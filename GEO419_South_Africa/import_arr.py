import rasterio as rio


def gdal_array(input_file):
    src = rio.open(input_file)
    arr = src.read()
    return arr