#import os
import numpy as np
from GEO419_South_Africa import ras_preprocessing, apply_along_axis, export_arr, function
from pathos import multiprocessing as mp
from datetime import datetime

start_time = datetime.now()

def main():
    # Input Folder Marlin:
    input_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/"
    # Input Folder Jonas:
    # input_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Testdaten/"

    # Input file name
    input_filename = "S1_A_VV_stack_mpumalanga_full_study_site_50m"

    # Output Folder Marlin:
    output_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/"
    # Output Folder Jonas:
    #output_folder = ""

    # Output File Name:
    output_file = input_filename + "_amp_if_test.tif"

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
    arr = ras_preprocessing.rio_array(input_file)
    result = apply_along_axis.parallel_apply_along_axis(func1d=function.amplitude_if_test, arr=arr, axis=0, cores=mp.cpu_count())
    export_arr.out_array(outname=outname, arr=result, input_file = input_file, dtype="int32")

### catch error of files dtype: ValueError: the array's dtype 'float32' does not match the file's dtype 'int32'  ####

    end_time = datetime.now()
    print("end-time = ", end_time-start_time, "Hr:min:sec")

# main func
if __name__ == '__main__':
    main()
