import numpy as np
import pathos.multiprocessing as mp
from skimage import io
import sys

np.set_printoptions(threshold=sys.maxsize)

arr = io.imread("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_subset.tif")
#arr = io.imread("C:/Users/jz199/Desktop/S1A_VH_Agulhas_50m_selected_bands_VH.tif")


def parallel_apply_along_axis(func1d, axis, arr, cores=16, *args, **kwargs):
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


shape = arr.shape


def np_fun(a):
    for i in range(0, shape[0]-1):
        # Returning the sum of elements at start index and at last index
        # inout array
        print(i)
        return (a[i])


print("axis=0 : ", np.apply_along_axis(np_fun, 1, arr))
print("\n")

print(shape)
#print("axis=1 : ", np.apply_along_axis(np_fun, 1, arr))



