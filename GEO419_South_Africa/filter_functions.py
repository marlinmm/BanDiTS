def mean_filter5(arr1d):
    import numpy as np
    kernel = (1 / 5.0) * np.ones((5))
    out = np.float32(np.convolve(arr1d, kernel, "valid"))
    return(out)


def mean_filter9(arr1d):
    import numpy as np
    kernel = (1 / 9.0) * np.ones((9))
    out = np.float32(np.convolve(arr1d, kernel, "valid"))
    return(out)


def median_filter5(arr1d):
    import scipy.signal as sig
    out = sig.medfilt(arr1d, kernel_size= 5)
    return out


def median_filter9(arr1d):
    import scipy.signal as sig
    out = sig.medfilt(arr1d, kernel_size= 9)
    return out


def median_filter11(arr1d):
    import scipy.signal as sig
    out = sig.medfilt(arr1d, kernel_size= 11)
    return out


def sobel_filter9(arr1d):
    import numpy as np
    kernel = [-5, -5, -5, -5, 0, 5, 5, 5, 5]
    out = np.float32(np.convolve(arr1d, kernel, "valid"))
    return out


def sobel_filter3(arr1d):
    import numpy as np
    kernel = [-5, 0, 5]
    out = np.float32(np.convolve(arr1d, kernel, "valid"))
    return out


def simple_edge_detection(arr1d):
    import numpy as np
    kernel = [-5, -5, -5, -5, 0, 5, 5, 5, 5]
    out = np.float32(np.convolve(arr1d, kernel, "valid"))
    if max(out) >= 30:
        return 1
    else:
        return 0
