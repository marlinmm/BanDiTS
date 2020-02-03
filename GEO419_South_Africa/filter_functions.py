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