#import os
import numpy as np
from GEO419_South_Africa import import_arr, apply_along_axis, export_arr, function
from pathos import multiprocessing as mp


def main():
    # Input Folder Marlin:
    # input_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/"
    # Input Folder Jonas:
    input_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Testdaten/"

    # Input file name
    input_filename = "S1A_VH_Agulhas_50m_selected_bands_VH_subset2.tif"

    # Output Folder Marlin:
    # output_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/"
    # Output Folder Jonas:
    output_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Output/"

    # Output File Name:
    output_file = "test_original_maximum.tif"

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
    result = apply_along_axis.parallel_apply_along_axis(func1d=function.maximum, arr=arr, axis=0, cores=mp.cpu_count())
    export_arr.out_array(outname=outname, arr=result, input_file = input_file)



# main func
if __name__ == '__main__':
    main()
