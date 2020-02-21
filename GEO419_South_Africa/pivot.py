def stdev_time(arr1d, stdev):
    """
    detects breakpoints through multiple standard deviations and devides breakpoints into timely separated sections (wanted_parts)
        - if sigma = 1      -> 68.3%
        - if sigma = 2      -> 95.5%
        - if sigma = 2.5    -> 99.0%
        - if sigma = 3      -> 99.7%
        - if sigma = 4      -> 99.9%
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel
    stdev: float
        number multiplied with standard deviation to define the probability space for a breakpoint

    Returns
    ----------
    numpy.int32
        0 = no breakpoint over time
        15 = breakpoint in the 1st section
        16 = breakpoint in the 2nd section
        17 = breakpoint in the 3rd section
        18 = breakpoint in the 4th section
        19 = breakpoint in the 5th section
        31 = breakpoint in the 1st AND 2nd section
        32 = breakpoint in the 1st AND 3rd section
        33 = breakpoint in the 1st AND 4th section OR breakpoint in the 2nd AND 3rd section
        34 = breakpoint in the 1st AND 5th section OR 2nd AND 4th section
        35 = breakpoint in the 2nd section AND 5th section OR 3rd AND 4th section
        36 = breakpoint in the 3rd AND 5th section
        37 = breakpoint in the 4th AND 5th section
        48 = breakpoint in the 1st, 2nd AND 3rd section
        49 = breakpoint in the 1st, 2nd AND 4th section
        50 = breakpoint in the 1st, 2nd AND 5th section OR 1st, 3rd AND 4th section
        51 = breakpoint in the 1st, 3rd AND 5th section OR 2nd, 3rd AND 4th section
        52 = breakpoint in the 1st, 3rd AND 5th section OR 2nd, 3rd AND 5th section
        53 = breakpoint in the 2nd, 4th AND 5th section
        54 = breakpoint in the 3rd, 4th AND 5th section
        66 = breakpoint in the 1st, 2nd, 3rd AND 4th section
        67 = breakpoint in the 1st, 2nd, 3rd AND 5th section
        68 = breakpoint in the 1st, 2nd, 4th AND 5th section
        69 = breakpoint in the 1st, 3rd, 4th AND 5th section
        70 = breakpoint in the 2nd, 3rd , 4th AND 5th section
        85 = breakpoints in all section
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
        std_mea = stdev*np.std(time_series_split[i])
        mini = min(time_series_split[i])
        sigma = mea - std_mea
        i +=1
        mini_list = [mini_list, mini]
        sigma_list = [sigma_list, sigma]        # weird list append, cause .append doesnt work with multiprocessing

    # check for dropping slope values from one fifth of time series to next
    temp = 0
    if mini_list[0][0][0][0][1] < sigma_list[0][0][0][0][1]:
       temp = temp + 15
    if mini_list[0][0][0][1] < sigma_list[0][0][0][1]:
       temp = temp + 16
    if mini_list[0][0][1] < sigma_list[0][0][1]:
      temp = temp + 17
    if mini_list[0][1] < sigma_list[0][1]:
      temp = temp + 18
    if mini_list[1] < sigma_list[1]:
      temp = temp + 19
    if temp == 0:
       return 0
    return temp

def amplitude_time(arr1d, threshold):
    """
    detects breakpoints through amplitude threshold and devides breakpoints into timely separated sections (wanted_parts)
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel
    threshold: float
        should be set between 4 and 10 for best results depending on use case

    Returns
    ----------
    numpy.int32
        0 = no breakpoint over time
        15 = breakpoint in the 1st section
        16 = breakpoint in the 2nd section
        17 = breakpoint in the 3rd section
        18 = breakpoint in the 4th section
        19 = breakpoint in the 5th section
        31 = breakpoint in the 1st AND 2nd section
        32 = breakpoint in the 1st AND 3rd section
        33 = breakpoint in the 1st AND 4th section OR breakpoint in the 2nd AND 3rd section
        34 = breakpoint in the 1st AND 5th section OR 2nd AND 4th section
        35 = breakpoint in the 2nd section AND 5th section OR 3rd AND 4th section
        36 = breakpoint in the 3rd AND 5th section
        37 = breakpoint in the 4th AND 5th section
        48 = breakpoint in the 1st, 2nd AND 3rd section
        49 = breakpoint in the 1st, 2nd AND 4th section
        50 = breakpoint in the 1st, 2nd AND 5th section OR 1st, 3rd AND 4th section
        51 = breakpoint in the 1st, 3rd AND 5th section OR 2nd, 3rd AND 4th section
        52 = breakpoint in the 1st, 3rd AND 5th section OR 2nd, 3rd AND 5th section
        53 = breakpoint in the 2nd, 4th AND 5th section
        54 = breakpoint in the 3rd, 4th AND 5th section
        66 = breakpoint in the 1st, 2nd, 3rd AND 4th section
        67 = breakpoint in the 1st, 2nd, 3rd AND 5th section
        68 = breakpoint in the 1st, 2nd, 4th AND 5th section
        69 = breakpoint in the 1st, 3rd, 4th AND 5th section
        70 = breakpoint in the 2nd, 3rd , 4th AND 5th section
        85 = breakpoints in all section
    """
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
    if diff_list[0][0][0][0][1] > threshold:
        temp = temp + 15
    if diff_list[0][0][0][1] > threshold:
        temp = temp + 16
    if diff_list[0][0][1] > threshold:
        temp = temp + 17
    if diff_list[0][1] > threshold:
        temp = temp + 18
    if diff_list[1] > threshold:
        temp = temp + 19
    if temp == 0:
        return 0
    return temp

def count_breakpoint(arr1d, height):
    """
    !!! STACK NEEDS TO BE MEDIAN- AND SOBEL-FILTERED BEFORE USE OF THIS FUNCTION (see filter_functions.py)!!!
    finds number of peaks greater than set height in median- and sobel-filtered time series for each pixel
    ----------
    arr1d: numpy.array
        1D array representing the time series for one pixel
    height: int
        should be set between 20 and 50 for best results;
        probably slightly higher for VH than for VV polarization

    Returns
    ----------
    numpy.int32
        returns either 1, if the time series contains one and only one peak higher than set threshold, otherwise 0
    """
    from scipy.signal import find_peaks
    peaks = find_peaks(arr1d, height=height)
    if len(peaks[0]) >= 3:
        return 3
    if len(peaks[0]) >= 2:
        return 2
    if len(peaks[0]) >= 1:
        return 1
    if len(peaks[0]) < 1:
        return 0
