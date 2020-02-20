def mean_filter(arr1d, kernel):
    import numpy as np
    kernel = (1 / float(kernel)) * np.ones((kernel))
    out = np.float32(np.convolve(arr1d, kernel, "valid"))
    return(out)


def median_filter(arr1d, kernel_size):
    import scipy.signal as sig
    import numpy as np
    out = np.float32(sig.medfilt(arr1d, kernel_size=kernel_size))
    return out


def sobel_filter(arr1d, kernel):
    import numpy as np
    out = np.float32(np.convolve(arr1d, kernel, "valid"))
    return out

