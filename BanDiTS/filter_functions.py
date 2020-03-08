def mean_filter(arr1d, kernel):
    """
    reference: https://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html
    simple mean filter for the time series applied along time axis in parallel_apply_along_axis()
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel
    kernel: int
         should be set between 3 and 21 for best results, but values need to be uneven, e.g. {"kernel": 3}

    Returns
    ----------
    numpy.ndarray
        returns mean-filtered numpy array
    """
    import numpy as np
    kernel = (1 / float(kernel)) * np.ones(kernel)
    # !!! ATTENTION: np.convolve with mode set to "valid" will cut n//2 values (kernel size = n) off the beginning and
    # end of the time series, bigger kernel sizes produces shorter time series with more data loss.
    out = np.float32(np.convolve(arr1d, kernel, "valid"))
    return out


def median_filter(arr1d, kernel):
    """
    reference: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.medfilt.html
    simple median filter for the time series applied along time axis in parallel_apply_along_axis()
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel
    kernel: int
         should be set between 3 and 21 for best results, but values need to be uneven, e.g. {"kernel": 3}

    Returns
    ----------
    numpy.ndarray
        returns median-filtered numpy array
    """
    import scipy.signal as sig
    import numpy as np
    out = np.float32(sig.medfilt(arr1d, kernel_size=kernel))
    return out


def sobel_filter(arr1d, kernel):
    """
    reference: https://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html
    !!! STACK SHOULD BE MEDIAN-FILTERED BEFORE USE OF THIS FUNCTION !!!
        (simply use median_filter() first and use output as new input)
    simple sobel filter for the time series applied along time axis in parallel_apply_along_axis()
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel
    kernel: int
         series of integers in a list, e. g. {"kernel": [-5, -5, 0, 5, 5]}
         should be set between 3 and 21 for best results, but values need to be uneven

    Returns
    ----------
    numpy.ndarray
        returns sobel-filtered numpy array
    """
    import numpy as np
    # !!! ATTENTION: np.convolve with mode set to "valid" will cut n//2 values (kernel size = n) off the beginning and
    # end of the time series, bigger kernel sizes produces shorter time series with more data loss.
    out = np.float32(np.convolve(arr1d, kernel, "valid"))
    return out
