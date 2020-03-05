import rasterio as rio
import numpy as np
import fiona


def fiona_shape(shape_path):
    """
    imports the specified shapefile to python
    ----------
    shape_path: string
        combined name of the input folder and file of the raster file

    Returns
    ----------
    fiona.collection.Collection
        returns shapefile in python readabale format
    """
    shapefile = fiona.open(shape_path, "r")
    return shapefile


def rio_array(input_file, hdr_file):
    """
    imports the specified rasterfile and if available the dates from the .hdr-file to python
    ----------
    input_file: string
        combined name of the input folder and file of the raster file
    hdr_file: string
        combined name of the input folder and file of the .hdr-file
    Returns
    ----------
    tuple
        return tuple containing the input raster file as a numpy array and the dates of each band, if a .hdr-file is
        available
    """
    # import of raster file
    src = rio.open(input_file)
    arr = src.read()
    all_dates = []

    # delete all bands with mostly -99 values (cheap and dirty detection)
    y_axis_len = arr.shape[1]   # length of y-axis
    x_axis_len = arr.shape[2]   # length of x-axis
    rotate_arr = arr
    rotate_arr = np.rollaxis(rotate_arr, 2)
    rotate_arr = np.rollaxis(rotate_arr, 2)
    rotate_arr = rotate_arr[y_axis_len // 2][x_axis_len // 2]   # get time series from center of image
    no_data = np.where(rotate_arr == -99.)  # get list of indices where value = -99
    arr = np.delete(arr, no_data[0], 0) # delete all bands with -99 values

    # get dates from corresponding hdr file
    if hdr_file != "":
        all_dates = date_import(hdr_file)
        all_dates = np.delete(all_dates, no_data[0], 0)

    return arr, all_dates


def date_import(hdr_file):
    """
    extracts the dates from a specified .hdr-file, if available
    ----------
    hdr_file: string
        combined name of the input folder and file of the .hdr-file
    Returns
    ----------
    list
        returns list conatining the dates of each band in the time series, according to the .hdr-file specified
    """
    raw_date_file = open(hdr_file, "r")
    date_string = raw_date_file.read()
    raw_date_file.close()
    start_index = date_string.find("band names = {")
    raw_date_string = date_string[start_index+14:len(date_string)-1]
    raw_date_list = raw_date_string.split(sep=", ")
    date_list = []
    for i in range(0, len(raw_date_list)):
        date_list.append(raw_date_list[i][raw_date_list[i].find("20"):raw_date_list[i].find("20")+8])
    return date_list

