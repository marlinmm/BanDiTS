from GEO419_South_Africa import import_arr


def preprocessing(input_file):
    import numpy as np
    arr = import_arr.rio_array(input_file)
    y_axis_len = arr.shape[1]
    x_axis_len = arr.shape[2]
    rotate_arr = arr
    rotate_arr = np.rollaxis(rotate_arr, 2)
    rotate_arr = np.rollaxis(rotate_arr, 2)
    rotate_arr = rotate_arr[y_axis_len//2][x_axis_len//2]
    no_data = np.where(rotate_arr == -99.        )
    arr = np.delete(arr, no_data[0], 0)
    return arr