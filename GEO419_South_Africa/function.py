import numpy as np

# func1d: functions to be applied on 1D array
def quantile(arr1d, percentile=0.5):
    import numpy as np
    return np.nanpercentile(arr1d, percentile)


def minimum(arr1d):
    import numpy as np
    return np.nanmin(arr1d)


def maximum(arr1d):
    import numpy as np
    return np.nanmax(arr1d)


def mean(arr1d):
    import numpy as np
    return np.nanmean(arr1d)
