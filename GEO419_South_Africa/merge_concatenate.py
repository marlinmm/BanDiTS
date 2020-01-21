import sys
from GEO419_South_Africa import import_arr, apply_along_axis
import rasterio as rio
import numpy as np
from pathos import multiprocessing as mp

np.set_printoptions(threshold=sys.maxsize)

# arr: full size numpy array 3D XxYxZ 200x300x100
arr = import_arr.gdal_array()
#print(arr)
#percentile = 5

# func1d: function to be applied on 1D array
def quantile(arr1d, percentile=0.5):
    import numpy as np
    return np.quantile(arr1d, percentile)

def minimum(arr1d):
    import numpy as np
    return np.min(arr1d)

def maximum(arr1d):
    import numpy as np
    return np.max(arr1d)

# result = parallel_apply_along_axis(func1d=quantile, arr=arr, axis=2, cores=4, **kw)

#result = apply_along_axis.parallel_apply_along_axis(func1d=quantile, arr=arr, axis=2, cores=4)
#print(result)
#print(result)



def parallel_apply_along_axis(func1d, axis, arr, cores=4, *args, **kwargs):
    import numpy as np
    """
    Like :func:`numpy.apply_along_axis()`, but takes advantage of multiple cores.
    Adapted from `here <https://stackoverflow.com/questions/45526700/
    easy-parallelization-of-numpy-apply-along-axis>`_.

    Parameters
    ----------
    func1d: function
        the function to be applied
    axis: int
        the axis along which to apply `func1d`
    arr: numpy.ndarray
        the input array
    cores: int
        the number of parallel cores
    args: any
        Additional arguments to `func1d`.
    kwargs: any
        Additional named arguments to `func1d`.
    Returns
    -------
    numpy.ndarray
    """
    # Effective axis where apply_along_axis() will be applied by each
    # worker (any non-zero axis number would work, so as to allow the use
    # of `np.array_split()`, which is only done on axis 0):
    effective_axis = 1 if axis == 0 else axis
    if effective_axis != axis:
        arr = arr.swapaxes(axis, effective_axis)

    def unpack(arguments):
        func1d, axis, arr, args, kwargs = arguments
        return np.apply_along_axis(func1d, axis, arr, *args, **kwargs)

    chunks = [(func1d, effective_axis, sub_arr, args, kwargs)
              for sub_arr in np.array_split(arr, mp.cpu_count())]

    pool = mp.Pool(cores)
    individual_results = pool.map(unpack, chunks)
    # Freeing the workers:
    pool.close()
    pool.join()

    return np.concatenate(individual_results)

def out_array():
    with rio.open(import_arr.filename) as src:
        ras_data = src.read()
        ras_meta = src.profile

    # make any necessary changes to raster properties, e.g.:
    ras_meta['dtype'] = "float32"
    ras_meta['nodata'] = -99

    with rio.open("C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/test1.tif", 'w', **ras_meta) as dst:
        dst.write(result, 1)


if __name__ == '__main__':
    result = parallel_apply_along_axis(func1d=minimum, arr=arr, axis=2, cores=16)
    print(result)
    out_array()