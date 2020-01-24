from pathos import multiprocessing as mp
import numpy as np


def parallel_apply_along_axis(func1d, axis, arr, cores, *args, **kwargs):
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
