import numpy as np


# func1d: functions to be applied on 1D array
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
    sigma = np.mean(arr1d) - 2 * np.std(arr1d)
    if diff >= 5:
        if np.min(arr1d) < sigma:
            return 1
        else:
            return 0
    else:
        return 0

def combined_density(arr1d):
    import numpy as np
    diff = np.max(arr1d) - np.min(arr1d)
    sigma25 = np.mean(arr1d) - 2.5 * np.std(arr1d)
    sigma3 = np.mean(arr1d) - 3 * np.std(arr1d)
    sigma4 = np.mean(arr1d) - 4 * np.std(arr1d)
    if diff >= 6:
        if np.min(arr1d) < sigma4:
            return 40
        if np.min(arr1d) < sigma3:
            return 30
        if np.min(arr1d) < sigma25:
            return 25
        # if np.min(arr1d) >= sigma25:
        else:
            return 0
    else:
        return 300


def amplitude_if_test(arr1d):
    import numpy as np
    diff = np.max(arr1d) - np.min(arr1d)
    if diff < 6:
        return 0
    if diff >= 6:
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
    #print(time_series_split[0])
    time_series_index_split = split_list(time_series_index, wanted_parts=5)
    #print(time_series_index_split[0])

    # calculate linear regression for each time series subarray
    slope_list = []
    for i in range (0,len(time_series_index_split)):
        slope, intercept, r_value, p_value, std_err = stats.linregress(time_series_split[i],time_series_index_split[i])
        i +=1
        slope_list = [slope_list, slope]        # weird list append, cause .append doesnt work with multiprocessing

    # check for dropping slope values from one fifth of time series to next
    temp = 0
    if slope_list[0][0][0][0][1] > 0 and slope_list[0][0][0][1] < 0:
        if slope_list[0][0][0][0][1] - slope_list[0][0][0][1] > 3:
            temp = temp + 1
        else:
            temp = 2
    if slope_list[0][0][0][1] > 0 and slope_list[0][0][1] < 0:
        if slope_list[0][0][0][1] - slope_list[0][0][1] > 3:
            temp = temp + 305
        else:
            temp = 400

    if slope_list[0][0][1] > 0 and slope_list[0][1] < 0:
        if slope_list[0][0][1] - slope_list[0][1] > 3:
            temp = temp + 500
        else:
            temp = temp + 600

    if slope_list[0][1] > 0 and slope_list[1] < 0:
        if slope_list[0][1] - slope_list[1] > 3:
            temp = temp + 700
        else:
            temp = temp + 800
    return temp


def stdev_time(arr1d):
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
    #print(time_series_split[0])
    #print("sdsdasdasd")
    time_series_index_split = split_list(time_series_index, wanted_parts=5)

    # calculate linear regression for each time series subarray
    mini_list = []
    sigma_list = []
    for i in range (0,len(time_series_index_split)):
        mea = np.mean(time_series_split[i])
        std_mea = 2.5*np.std(time_series_split[i])
        mini = min(time_series_split[i])
        sigma = mea - std_mea
        i +=1
        mini_list = [mini_list, mini]
        sigma_list = [sigma_list, sigma]        # weird list append, cause .append doesnt work with multiprocessing

    # check for dropping slope values from one fifth of time series to next
    temp = 0
    # if mini_list[0][0][0][0][1] < sigma_list[0][0][0][0][1]:
    #   temp = temp + 15
    # if mini_list[0][0][0][1] < sigma_list[0][0][0][1]:
    #   temp = temp + 16
    if mini_list[0][0][1] < sigma_list[0][0][1]:
      temp = temp + 17
    if mini_list[0][1] < sigma_list[0][1]:
      temp = temp + 18
    if mini_list[1] < sigma_list[1]:
      temp = temp + 19
    if temp == 0:
       return 0
    return temp

def amplitude_time(arr1d):
        import numpy as np
        from scipy import stats
        time_series = arr1d
        arr_shape = arr1d.shape[0]
        time_series_index = np.indices((arr_shape,))[0]

        # internal function to split time series in n sub time series
        def split_list(alist, wanted_parts=1):  # based on: https://stackoverflow.com/a/752562
            length = len(alist)
            return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
                    for i in range(wanted_parts)]

        # split time series and list of time series indices in 4 subarrays
        time_series_split = split_list(time_series, wanted_parts=5)
        # print(time_series_split[0])
        # print("sdsdasdasd")
        time_series_index_split = split_list(time_series_index, wanted_parts=5)

        # calculate linear regression for each time series subarray
        diff_list = []
        for i in range(0, len(time_series_index_split)):
            maxi = max(time_series_split[i])
            mini = min(time_series_split[i])
            diff = maxi - mini
            i += 1

            diff_list = [diff_list, diff]  # weird list append, cause .append doesnt work with multiprocessing

        # check for dropping slope values from one fifth of time series to next
        temp = 0
        # if diff_list[0][0][0][0][1] > 6:
        #   temp = temp + 15
        # if diff_list[0][0][0][1] > 6:
        #     temp = temp + 16
        if diff_list[0][0][1] > 5:
            temp = temp + 17
        if diff_list[0][1] > 5:
            temp = temp + 18
        if diff_list[1] > 5:
            temp = temp + 19
        if temp == 0:
            return 0
        return temp


def find_peaksVH(arr1d):
    from scipy.signal import find_peaks
    peaks = find_peaks(arr1d, height=30)
    if len(peaks[0]) >= 3:
        return 3
    if len(peaks[0]) >= 2:
        return 2
    if len(peaks[0]) >= 1:
        return 1
    if len(peaks[0]) < 1:
        return 0


def find_peaksVV(arr1d):
    from scipy.signal import find_peaks
    peaks = find_peaks(arr1d, height=25)
    if len(peaks[0]) >= 3:
        return 3
    if len(peaks[0]) >= 2:
        return 2
    if len(peaks[0]) >= 1:
        return 1
    if len(peaks[0]) < 1:
        return 0


def percentile(arr1d):
    import numpy as np
    upper = np.percentile(arr1d, 99)
    lower = np.percentile(arr1d, 1)
    return upper - lower

    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.percentile.html
    # def quantile(arr1d, percentile=90):
    #     import numpy as np
    #     return np.percentile(arr1d, percentile)



# Recurrence matrix:
# https://pypi.org/project/PyRQA/
# http://www.pik-potsdam.de/~donges/pyunicorn/api/timeseries/recurrence_plot.html


# Convolution -> for use in filtering
# http://juanreyero.com/article/python/python-convolution.html
# https://stackoverflow.com/questions/20036663/understanding-numpys-convolve


