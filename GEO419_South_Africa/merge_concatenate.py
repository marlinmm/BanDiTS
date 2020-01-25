#import os
import numpy as np
from GEO419_South_Africa import import_arr, apply_along_axis, export_arr
from pathos import multiprocessing as mp


def main():
    # Input Folder Marlin:
    input_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/"
    # Input Folder Jonas:
    # input_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Testdaten/"

    # Input file name
    input_filename = "S1A_VH_Agulhas_50m_selected_bands_VH.tif"

    # Output Folder Marlin:
    output_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/"
    # Output Folder Jonas:
    #output_folder = ""

    # Output File Name:
    output_file = "test_original_mean.tif"

    ######################   NO USER INPUT BEYOND THIS POINT   ###############################

    # example of changeble output names
        # basename = 'out{}.tif'
        # tuning = 3
        # outname = os.path.join(input_folder, basename.format(tuning))

    # example of new sub directory creation
        # subdir = os.path.join(input_folder, 'sub')
        # os.makedirs(subdir, exist_ok=True)

    input_file = input_folder + input_filename
    outname = output_folder + output_file

    # arr: full size numpy array 3D XxYxZ 200x300x100
    arr = import_arr.rio_array(input_file)
    #arr[arr == -99] = np.nan ## trying to loose -99 values cause it corrupts output map
    result = apply_along_axis.parallel_apply_along_axis(func1d=mean, arr=arr, axis=0, cores=mp.cpu_count())
    export_arr.out_array(outname=outname, arr=result, input_file = input_file)



# func1d: functions to be applied on 1D array
def quantile(arr1d, percentile=0.5):
    import numpy as np
    return np.quantile(arr1d, percentile)


def minimum(arr1d):
    import numpy as np
    return np.min(arr1d)


def maximum(arr1d):
    import numpy as np
    return np.max(arr1d)


def mean(arr1d):
    import numpy as np
    return np.mean(arr1d)


# main func
if __name__ == '__main__':
    main()
