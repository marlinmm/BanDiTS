import rasterio as rio
import numpy as np
import fiona

def fiona_shape(shape_path):
    shapefile = fiona.open(shape_path, "r")
    return shapefile


def rio_array(input_file):
    # import of raster file
    src = rio.open(input_file)
    arr = src.read()
    # delete all bands with mostly -99 values (cheap and dirty detection)
    y_axis_len = arr.shape[1]   # length of y-axis
    x_axis_len = arr.shape[2]   # length of x-axis
    rotate_arr = arr
    rotate_arr = np.rollaxis(rotate_arr, 2)
    rotate_arr = np.rollaxis(rotate_arr, 2)

    rotate_arr = rotate_arr[y_axis_len // 2][x_axis_len // 2]   # get time series from center of image
    no_data = np.where(rotate_arr == -99.)  # get list of indices where value = -99
    arr = np.delete(arr, no_data[0], 0) # delete all bands with -99 values

    # only for "aghulas test site" to delete 2 layers, where top third was -99
    if len(no_data[0]) > 0:
        arr = np.delete(arr, 16, 0)
        arr = np.delete(arr, 26, 0)
        return arr
    else:
        return arr
