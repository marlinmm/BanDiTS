import numpy as np


# func1d: functions to be applied on 1D array
def quantile(arr1d, percentile=0.5):
    import numpy as np
    return np.percentile(arr1d, percentile)


def minimum(arr1d):
    import numpy as np
    return np.min(arr1d)


def maximum(arr1d):
    import numpy as np
    return np.max(arr1d)


def mean(arr1d):
    import numpy as np
    return np.mean(arr1d)


def amplitude_if_test(arr1d):
    import numpy as np
    diff = np.max(arr1d) - np.min(arr1d)
    if diff < 7.5:
        return 0
    if diff >= 7.5:
        return 1


def stdev(arr1d):
    import numpy as np
    return np.std(arr1d)


def slope(arr1d):
    import numpy as np
    from scipy import stats
    #print(arr1d.shape)
    x = arr1d
    #print(x)
    y = np.indices((119,))
    #print(y)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    return slope

    #print(len(arr1d))