import os
import numpy as np
from datetime import datetime
from BanDiTS import preprocessing, apply_along_axis, export_arr
from BanDiTS.statistical_functions import *
from BanDiTS.filter_functions import *
from BanDiTS.breakpoint_functions import *
from pathos import multiprocessing as mp


def main():
    ###################################     INPUT    ########################################

    # Input Folder:
    raster_folder = "/example/path/to/input/folder/"

    # Input File Name
    raster_filename = "example_file_name"

    ###################################     OUTPUT    ########################################

    # Output Folder:
    output_folder = "/example/path/to/output/folder/"

    ####################### USER-DEPENDENT FILTER-FUNCTIONS TO BE USED #######################
    # Example for mean filter:
    # filter_functions = [mean_filter, mean_filter, mean_filter]
    # filter_args = [{"kernel": 3}, {"kernel": 9}, {"kernel": 13}]

    # Example for median filter:
    # filter_functions = [median_filter, median_filter, median_filter]
    # filter_args = [{"kernel": 3}, {"kernel": 9}, {"kernel": 13}]

    # Example for Sobel filter:
    filter_functions = [sobel_filter, sobel_filter, sobel_filter]
    filter_args = [{"kernel": [-5, 0, 5]}, {"kernel": [-5, -5, 0, 5, 5]}, {"kernel": [-5, -5, -5, -5, 0, 5, 5, 5, 5]}]

    ################### USER-DEPENDENT STATISTICAL FUNCTIONS TO BE USED ######################
    # Example for statistical function:
    statistical_functions = [percentile, median]
    statistical_args = [{"upper": 95, "lower": 5}, {}]

    ###################### USER-DEPENDENT BREAKPOINT FUNCTIONS TO BE USED ####################
    # Example for breakpoint functions (APPLY ONLY AFTER MEDIAN- AND SOBEL-FILTER!!!):
    breakpoint_functions = [count_breakpoint]
    breakpoint_args = [{"threshold": 120}]

    ######################   NO USER INPUT BEYOND THIS POINT   ###############################

    return raster_folder, raster_filename, output_folder, filter_functions, filter_args, statistical_functions, \
        statistical_args, breakpoint_functions, breakpoint_args


def filter_func(raster_folder, raster_filename, output_folder, filter_functions, filter_args):
    start_time = datetime.now()
    input_raster = os.path.join(raster_folder, raster_filename)
    hdr_file = ""   # only used for ENVI stacks
    outname = os.path.join(output_folder, raster_filename)
    if outname.find(".tif") != -1:
        outname = outname[0:len(outname) - 4]

    # arr: full size numpy array 3D XxYxZ 200x300x100
    arr = preprocessing.rio_array(input_raster, hdr_file=hdr_file)

    # activate to get list of dates from .hdr file (.hdr file needs to be specified above)
    # dates = arr[1]

    for i, func in enumerate(filter_functions):
        kernel_size = str(filter_args[i]['kernel'])
        filtered_arr = apply_along_axis.parallel_apply_along_axis(func1d=func, arr=arr[0], axis=0, cores=mp.cpu_count(),
                                                                  **filter_args[i])
        filtered_arr = np.rollaxis(filtered_arr, 2)
        filtered_arr = np.rollaxis(filtered_arr, 1)
        filtered_arr = np.rollaxis(filtered_arr, 2)

        dtype = type(filtered_arr[0][0][0])
        func_name_end = str(func).find(" at")
        func_name_start = 10
        func_name = str(func)[func_name_start:func_name_end]

        # exporting result to new raster
        export_arr.functions_out_array(outname=outname + "_" + func_name + str(kernel_size), arr=filtered_arr,
                                       input_file=input_raster, dtype=dtype)
    # print time to this point
    filter_time = datetime.now()
    print("filter-time = ", filter_time - start_time, "Hr:min:sec")


def statistics_func(raster_folder, raster_filename, output_folder, statistical_functions, statistical_args):
    start_time = datetime.now()
    input_raster = os.path.join(raster_folder, raster_filename)
    hdr_file = ""  # input_raster + ".hdr"        # only used for ENVI stacks
    outname = os.path.join(output_folder, raster_filename)
    if outname.find(".tif") != -1:
        outname = outname[0:len(outname) - 4]

    # arr: full size numpy array 3D XxYxZ 200x300x100
    arr = preprocessing.rio_array(input_raster, hdr_file=hdr_file)

    # activate to get list of dates from .hdr file (.hdr file needs to be specified above)
    # dates = arr[1]

    for i, func in enumerate(statistical_functions):
        # creating results with calling wanted algorithm in parallel_apply_along_axis for quick runtime
        result = apply_along_axis.parallel_apply_along_axis(func1d=func, arr=arr[0], axis=0, cores=mp.cpu_count(),
                                                            **statistical_args[i])

        # selecting dtype based on result
        dtype = type(result[0][0])

        func_name_end = str(func).find(" at")
        func_name_start = 10
        func_name = str(func)[func_name_start:func_name_end]

        # exporting result to new raster
        export_arr.functions_out_array(outname=outname + "_" + func_name + str(i), arr=result, input_file=input_raster,
                                       dtype=dtype)
    # print time to this point
    statistics_time = datetime.now()
    print("breakpoint-time = ", statistics_time - start_time, "Hr:min:sec")


def breakpoint_func(raster_folder, raster_filename, output_folder, breakpoint_functions, breakpoint_args):
    start_time = datetime.now()
    input_raster = os.path.join(raster_folder, raster_filename)
    hdr_file = ""   # only used for ENVI stacks
    outname = os.path.join(output_folder, raster_filename)
    if outname.find(".tif") != -1:
        outname = outname[0:len(outname) - 4]

    # arr: full size numpy array 3D XxYxZ 200x300x100
    arr = preprocessing.rio_array(input_raster, hdr_file=hdr_file)

    # activate to get list of dates from .hdr file (.hdr file needs to be specified above)
    # dates = arr[1]

    for i, func in enumerate(breakpoint_functions):
        threshold_size = str(breakpoint_args[i]['threshold'])
        result = apply_along_axis.parallel_apply_along_axis(func1d=func, arr=arr[0], axis=0, cores=mp.cpu_count(),
                                                            **breakpoint_args[i])
        # selecting dtype based on result
        dtype = type(result[0][0])

        func_name_end = str(func).find(" at")
        func_name_start = 10
        func_name = str(func)[func_name_start:func_name_end]

        # exporting result to new raster
        export_arr.functions_out_array(outname=outname + "_" + func_name + str(threshold_size), arr=result,
                                       input_file=input_raster, dtype=dtype)
    # print time to this point
    filter_time = datetime.now()
    print("filter-time = ", filter_time - start_time, "Hr:min:sec")


if __name__ == '__main__':
    start_time = datetime.now()
    in_variables = main()

    # call this function to execute filter functions:
    filter_func(raster_folder=str(in_variables[0]), raster_filename=str(in_variables[1]),
                output_folder=str(in_variables[2]), filter_functions=in_variables[3],
                filter_args=in_variables[4])

    # call this function to execute statistics functions:
    # statistics_func(raster_folder=str(in_variables[0]), raster_filename=str(in_variables[1]),
    #                 output_folder=str(in_variables[2]), statistical_functions=in_variables[5],
    #                 statistical_args=in_variables[6])

    # call this function to execute breakpoint functions:
    # breakpoint_func(raster_folder=str(in_variables[0]), raster_filename=str(in_variables[1]),
    #                 output_folder=str(in_variables[2]), breakpoint_functions=in_variables[7],
    #                 breakpoint_args=in_variables[8])
