import os
import sys
from GEO419_South_Africa import import_arr
from GEO419_South_Africa import apply_along_axis
import rasterio as rio
import numpy as np
from pathos import multiprocessing as mp


def main():

    workdir = ''
    # workdir = ''
    ####################################################
    # no user input beyond this line
    basename = 'out{}.tif'

    tuning = 3

    subdir = os.path.join(workdir, 'sub')
    os.makedirs(subdir, exist_ok=True)


    outname = os.path.join(workdir, basename.format(tuning))

    np.set_printoptions(threshold=sys.maxsize)

    # arr: full size numpy array 3D XxYxZ 200x300x100
    arr = import_arr.gdal_array()

    # trying to rotate array, doesnt really do anything...
    #arr = np.rollaxis(arr, 2)
    #arr = np.rollaxis(arr, 2)
    print(arr.shape)
    #print(arr)
    #percentile = 5

    result = apply_along_axis.parallel_apply_along_axis(func1d=maximum, arr=arr, axis=0, cores=mp.cpu_count())
    #print(result)
    outname = "C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/test_ultrahuge_max.tif"
    out_array(outname=outname, arr=result)


# func1d: functions to be applied on 1D array
def quantile(arr1d, percentile=0.5):
    import numpy as np
    return np.quantile(arr1d, percentile)


def minimum(arr1d):
    import numpy as np
    return np.min(arr1d)


def maximum(arr1d):
    import numpy as np
    return np.max(arr1d)


def mean(arr1d):
    import numpy as np
    return np.mean(arr1d)


# function to generate output tif
def out_array(outname, arr):
    with rio.open(import_arr.filename) as src:
        ras_data = src.read()
        ras_meta = src.profile

    # make any necessary changes to raster properties, e.g.:
    ras_meta['dtype'] = "float32"
    ras_meta['nodata'] = -99

    #with rio.open("C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/test3456_7.tif", 'w', **ras_meta) as dst:
    with rio.open(outname, 'w', **ras_meta) as dst:
        dst.write(arr, 1)


# main func
if __name__ == '__main__':
    main()
