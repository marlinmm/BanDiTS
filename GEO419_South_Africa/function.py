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
    x = arr1d
    arr_shape = arr1d.shape[0]
    y = np.indices((arr_shape,))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    return slope


def slope_vs_slope(arr1d):
    import numpy as np
    from scipy import stats
    x = arr1d
    arr_shape = arr1d.shape[0]
    #print(x)
    y = np.indices((arr_shape,))[0]
    #print("orig: " + str(y))
    def split_list(alist, wanted_parts=1):          # based on: https://stackoverflow.com/a/752562
        length = len(alist)
        return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
                for i in range(wanted_parts)]
    x_split = split_list(x, wanted_parts=4)
    #print(x_split[0])
    y_split = split_list(y, wanted_parts=4)
    #print(y_split[0])
    slope_list = []
    for i in range (0,len(y_split)):
        slope, intercept, r_value, p_value, std_err = stats.linregress(x_split[i],y_split[i])
        i +=1
        slope_list = [slope_list, slope]

    #print(l[1])
    #print(l[0][1])
    #print(l[0][0][1])
    #print(l[0][0][0][1])

    if slope_list[0][0][0][1] > 0 and slope_list[0][0][1] < 0:
        if slope_list[0][0][0][1] - slope_list[0][0][1] > 3:
            return 1
        else:
            return 2

    if slope_list[0][0][1] > 0 and slope_list[0][1] < 0:
        if slope_list[0][0][1] - slope_list[0][1] > 3:
            return 3
        else:
            return 4

    if slope_list[0][1] > 0 and slope_list[1] < 0:
        if slope_list[0][1] - slope_list[1] > 3:
            return 5
        else:
            return 6
    else:
        return 0
    #print(slope_list)
    #return slope

    #### UNFERTIG ####


#def mean_2sigma():
