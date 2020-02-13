# func1d: functions to be applied on 1D array
def minimum(arr1d):
    """
    calculates the minimum of the time series for one pixel
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel

    Returns
    -------
    numpy.float64
        minimum of the time series for one pixel
    """
    import numpy as np
    return np.min(arr1d)


def maximum(arr1d):
    """
    calculates the maximum of the time series for one pixel
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel

    Returns
    -------
    numpy.float64
        maximum of the time series for one pixel
    """
    import numpy as np
    return np.max(arr1d)


def mean(arr1d):
    """
    calculates the mean of the time series for one pixel
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel

    Returns
    -------
    numpy.float64
        mean of the time series for one pixel
    """
    import numpy as np
    return np.mean(arr1d)


def stdev(arr1d):
    """
    calculates the standard deviation of the time series for one pixel
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel

    Returns
    -------
    numpy.float64
        standard deviation of the time series for one pixel
    """
    import numpy as np
    return np.std(arr1d)

def median(arr1d):
    """
    calculates the median of the time series for one pixel
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel

    Returns
    -------
    numpy.float64
        median of the time series for one pixel
    """
    import numpy as np
    return np.median(arr1d)


def improved_stdev(arr1d):
    """
    calculates the 95% probability space of each time series and checks if the minimum value falls within the
    95% intervall or not
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel

    Returns
    -------
    numpy.int32
        returns either 1, if the minimum value is lower than the mean values minus two times the standard deviation
        or returns 0 if this is not the case
    """
    import numpy as np
    diff1 = np.mean(arr1d)-2*np.std(arr1d)
    if np.min(arr1d) < diff1:
        return 1
    else:
        return 0


### def threshold(arr1d, threshold):
def simple_threshold(arr1d):
    """
    simple threshold function, which checks, if the minimum value of the time series falls below a certain threshold
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel
    ### threshold: int
    ###    should be set between -15 and -25 for best results depending on use case
    ### DOESNT WORK LIKE THAT
    Returns
    -------
    numpy.int32
        returns either 1, if the minimum value is lower than the set threshold or returns 0 if this is not the case
    """
    import numpy as np
    threshold = -20
    if np.min(arr1d) < threshold:
        return 1
    else:
        return 0


def combined(arr1d):
    ### ADD DOCSTRING ###

    import numpy as np
    diff = np.max(arr1d) - np.min(arr1d)
    sigma = np.mean(arr1d) - 2 * np.std(arr1d)
    if diff >= 7:
        if np.min(arr1d) < sigma:
            return 1
        else:
            return 0
    else:
        return 0


def amplitude_if_test(arr1d):
    """
    calculates the amplitude of the time series and applies a threshold for the amplitude
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel
    threshold: int
        should be set between 4 and 10 for best results depending on use case

    Returns
    -------
    numpy.int32
        returns either 1, if the amplitude value is higher than the set threshold or returns 0 if this is not the case
    """
    import numpy as np
    diff = np.max(arr1d) - np.min(arr1d)
    if diff < 8:
        return 0
    if diff >= 6:
        return 1


def slope(arr1d):
    """
    calculates the slope for the whole time series for one pixel
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel

    Returns
    -------
    numpy.float64
        returns slope value of the time series for one pixel
    """
    import numpy as np
    from scipy import stats
    x = arr1d
    arr_shape = arr1d.shape[0]
    y = np.indices((arr_shape,))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    return slope


def slope_vs_slope(arr1d):
    """
    calculates the slopes for subsections of the time series for one pixel and compares the negative slope change from
    time n-n and n-n+1, the n-n+1 and n-n+2 until n-1 and n. During this process a value for each result is created
    allowing the user to extract info on a slope change at a specific time, e.g. the value 1 means a negative slope
    change between section 1 and 2 of the time series, the value 501 means a negative slope change between section 1
    and 2 and also a negative slope change between section 3 and 4. End values containing the numbers 2, 400, 600 and
    800 mean that there was no negative slope change detected in the corresponding time frame
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel

    Returns
    -------
    numpy.int32
        0 = no negative slope change detected
        1 = negative slope change between time frame 1 and 2
        2 = see 0
        305 = negative slope change between time frame 2 and 3
        400 = see 0
        500 = negative slope change between time frame 3 and 4
        501 = negative slope change between time frame 3 and 4 and time frame 1 and 2
        502 = see 500
        600 = see 0
        601 = see 1
        602 = see 0
        700 = negative slope change between time frame 4 and 5
        701 = negative slope change between time frame 4 and 5 and time frame 1 and 2
        702 = see 700
        800 = see 0
        1005 = negative slope change between time frame 4 and 5 and time frame 2 and 3
        1100 = see 700
        1105 = see 305
        1200 = see 0
    """
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

    # split time series and list of time series indices in 5 subarrays
    time_series_split = split_list(time_series, wanted_parts=5)
    time_series_index_split = split_list(time_series_index, wanted_parts=5)

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


def combined_time(arr1d):
    ### ADD DOCSTRING ###

    import numpy as np
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

    # calculate mean, stdev and minimum of each subarray
    mini_list = []
    sigma_list = []
    for i in range (0,len(time_series_index_split)):
        mea = np.mean(time_series_split[i])
        std_mea = 2*np.std(time_series_split[i])
        mini = min(time_series_split[i])
        sigma = mea - std_mea
        i +=1
        mini_list = [mini_list, mini]
        sigma_list = [sigma_list, sigma]        # weird list append, cause .append doesnt work with multiprocessing

    # check, if minimum of time n is smaller than 2 sigma probability space
    temp = 0
    # if mini_list[0][0][0][0][1] < sigma_list[0][0][0][0][1]:      # first time frame
    #     return 1
    if mini_list[0][0][0][1] < sigma_list[0][0][0][1]:              # second time frame
      return 1
    # if mini_list[0][0][1] < sigma_list[0][0][1]:                  # third time frame
    #   return 1
    # if mini_list[0][1] < sigma_list[0][1]:                        # fourth time frame
    #   return 1
    # if mini_list[1] < sigma_list[1]:                              # fifth time frame
    #   return 1
    else:
        return 0
    return temp
    ### NOT WORKING PROPERLY ###

### def find_peaks(arr1d, threshold):
def find_peaks(arr1d):
    """
    !!! STACK NEEDS TO BE MEDIAN- AND SOBEL-FILTERED BEFORE USE OF THIS FUNCTION (see filter_functions.py)!!!
    finds peaks greater than set height in median- and sobel-filtered time series for each pixel if there is only one
    peak in the time series
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel
    ### threshold: int
    ###     should be set between 20 and 50 for best results
    ### DOESNT WORK LIKE THAT

    Returns
    -------
    numpy.int32
        returns either 1, if the time series contains one and only one peak higher than set threshold, otherwise 0
    """
    from scipy.signal import find_peaks
    threshold = 35
    peaks = find_peaks(arr1d, height=threshold)
    if len(peaks[0]) >= 2 or len(peaks[0]) == 0:
        return 0
    if len(peaks[0]) == 1:
        return 1


def find_troughs(arr1d):
    from scipy.signal import find_peaks
    peaks = find_peaks(-1*arr1d, height=40)
    if len(peaks[0]) >= 1:
        return 1
    if len(peaks[0]) < 1:
        return 0
    ### NOT WORKING PROPERLY ###


def percentile(arr1d):
    import numpy as np
    upper = np.percentile(arr1d, 90)
    lower = np.percentile(arr1d, 10)
    return upper - lower


# Recurrence matrix:
# https://pypi.org/project/PyRQA/
# http://www.pik-potsdam.de/~donges/pyunicorn/api/timeseries/recurrence_plot.html


# Convolution -> for use in filtering
# http://juanreyero.com/article/python/python-convolution.html
# https://stackoverflow.com/questions/20036663/understanding-numpys-convolve