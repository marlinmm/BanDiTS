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


def stdev(arr1d):
    import numpy as np
    return np.std(arr1d)


def improved_stdev(arr1d):
    import numpy as np
    diff1 = np.mean(arr1d)-2.5*np.std(arr1d)
    if np.min(arr1d) < diff1:
        return 1
    else:
        return 0


def threshold(arr1d):
    import numpy as np
    if np.min(arr1d) < -21:
        return 1
    else:
        return 0


def combined(arr1d):
    import numpy as np
    diff = np.max(arr1d) - np.min(arr1d)
    sigma = np.mean(arr1d) - 3 * np.std(arr1d)
    if diff >= 6:
        if np.min(arr1d) < sigma:
            return 1
        else:
            return 0
    else:
        return 0


def amplitude_if_test(arr1d):
    import numpy as np
    diff = np.max(arr1d) - np.min(arr1d)
    if diff < 8:
        return 0
    if diff >= 8:
        return 1


def slope(arr1d):
    import numpy as np
    from scipy import stats
    x = arr1d
    arr_shape = arr1d.shape[0]
    y = np.indices((arr_shape,))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    return slope


def slope_vs_slope(arr1d):
    import numpy as np
    from scipy import stats
    time_series = arr1d
    arr_shape = arr1d.shape[0]
    time_series_index = np.indices((arr_shape,))[0]

    # internal function to split time series in n sub time series
    def split_list(alist, wanted_parts=1):          # based on: https://stackoverflow.com/a/752562
        length = len(alist)
        return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
                for i in range(wanted_parts)]

    # split time series and list of time series indices in 4 subarrays
    time_series_split = split_list(time_series, wanted_parts=5)
    time_series_index_split = split_list(time_series_index, wanted_parts=5)
    slope_list = []

    # calculate linear regression for each time series subarray
    for i in range (0,len(time_series_index_split)):
        slope, intercept, r_value, p_value, std_err = stats.linregress(time_series_split[i],time_series_index_split[i])
        i +=1
        slope_list = [slope_list, slope]        # weird list append, cause .append doesnt work with multiprocessing

    # check for dropping slope values from one fifth of time series to next
    x = 0
    if slope_list[0][0][0][0][1] > 0 and slope_list[0][0][0][1] < 0:
        if slope_list[0][0][0][0][1] - slope_list[0][0][0][1] > 3:
            x = x + 1
        else:
            x = 2
    if slope_list[0][0][0][1] > 0 and slope_list[0][0][1] < 0:
        if slope_list[0][0][0][1] - slope_list[0][0][1] > 3:
            x = x + 305
        else:
            x = 400

    if slope_list[0][0][1] > 0 and slope_list[0][1] < 0:
        if slope_list[0][0][1] - slope_list[0][1] > 3:
            x = x + 500
        else:
            x = x + 600

    if slope_list[0][1] > 0 and slope_list[1] < 0:
        if slope_list[0][1] - slope_list[1] > 3:
            x = x + 700
        else:
            x = x + 800
    # else:
    #     x = 100
    return x


def percentile_year(arr1d):
    import numpy as np
    # do stuff here
    np.percentile(arr1d)
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.percentile.html


# recurrence matrix
# https://pypi.org/project/PyRQA/
# http://www.pik-potsdam.de/~donges/pyunicorn/api/timeseries/recurrence_plot.html