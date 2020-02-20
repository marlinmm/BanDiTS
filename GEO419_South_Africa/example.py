from GEO419_South_Africa import preprocessing, apply_along_axis, export_arr, filter_functions, function
from GEO419_South_Africa.filter_functions import *
from GEO419_South_Africa.function import *
from pathos import multiprocessing as mp
from datetime import datetime
import numpy as np

start_time = datetime.now()


def main():
    ###################################     INPUT    ########################################

    # Input Folder Marlin:
    raster_folder = "C:/Users/marli/Desktop/Marcel_Daten/Original/"
    # Input Folder Jonas:
    # raster_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester\Vorlesungsmitschriften/GEO402 - Ableitung von Landoberflächenparametern/Subset/"

    # Input file name
    raster_filename = "S1_A_VH_stack_pilanesberg_full_scene_50m_center.tif"
    # raster_filename = "SubsetVH.tif"

    ###################################     OUTPUT    ########################################

    # Output Folder Marlin:
    output_folder = "C:/Users/marli/Desktop/Marcel_Daten/Output/"
    # Output Folder Jonas:
    # output_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester\Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Output/"

    # time series functions to be applied; see function.py for options
    functions = [median_filter]

    args = [{"kernel_size": 9}]
    #args = [{'kernel': 9}, {'kernel_size': 5}, {'kernel': [-5, -5, -5, -5, 0, 5, 5, 5, 5]}]

    # Output File Name:
    # output_file = raster_file name[0:len(raster_filename)-4] + "_median_filtered3.tif"
    output_file = raster_filename
    return raster_folder, raster_filename, output_folder, functions, args

    ######################   NO USER INPUT BEYOND THIS POINT   ###############################


def filter(raster_folder, raster_filename, output_folder, functions, args):
    input_raster = raster_folder + raster_filename
    hdr_file = ""#input_raster + ".hdr"
    outname = output_folder + raster_filename

    # arr: full size numpy array 3D XxYxZ 200x300x100
    arr = preprocessing.rio_array(input_raster, hdr_file=hdr_file)
    dates = arr[1]

    # jupyter notebook
    # infile = '../rasterstack'

    for i, func in enumerate(functions):
        filtered_arr = apply_along_axis.parallel_apply_along_axis(func1d=func, arr=arr[0], axis=0, cores=mp.cpu_count(),
                                                                  **args[i])
        filtered_arr = np.rollaxis(filtered_arr, 2)
        filtered_arr = np.rollaxis(filtered_arr, 1)
        filtered_arr = np.rollaxis(filtered_arr, 2)

        dtype = type(filtered_arr[0][0][0])
        func_name_end = str(func).find(" at")
        func_name_start = 10
        func_name = str(func)[func_name_start:func_name_end]

        export_arr.functions_out_array(outname=outname + "_" + func_name, arr=filtered_arr, input_file=input_raster,
                                       dtype=dtype)

        end_time = datetime.now()
        print("end-time = ", end_time - start_time, "Hr:min:sec")


def breakpoint(raster_folder, raster_filename, output_folder, functions, args):
    input_raster = raster_folder + raster_filename
    hdr_file = input_raster + ".hdr"
    outname = output_folder + raster_filename

    # arr: full size numpy array 3D XxYxZ 200x300x100
    arr = preprocessing.rio_array(input_raster, hdr_file=hdr_file)
    dates = arr[1]

    # jupyter notebook
    infile = '../rasterstack'

    for i, func in enumerate(functions):
        # creating results with calling wanted algorithm in parallel_apply_along_axis for quick runtime
        result = apply_along_axis.parallel_apply_along_axis(func1d=func, arr=arr[0], axis=0,
                                                            cores=mp.cpu_count(), **args[i])

        # selecting dtype based on result
        dtype = type(result[0][0])

        func_name_end = str(func).find(" at")
        func_name_start = 10
        func_name = str(func)[func_name_start:func_name_end]

        # exporting result to new raster
        export_arr.functions_out_array(outname=outname + "_" + func_name, arr=result, input_file=input_raster,
                                       dtype=dtype)

        end_time = datetime.now()
        print("end-time = ", end_time - start_time, "Hr:min:sec")


# main func
if __name__ == '__main__':
    in_variables = main()
    filter(raster_folder=str(in_variables[0]), raster_filename=str(in_variables[1]),
           output_folder=str(in_variables[2]), functions=in_variables[3], args=in_variables[4])
    #breakpoint(raster_folder=str(in_variables[0]), raster_filename=str(in_variables[1]),
    #           output_folder=str(in_variables[2]), functions=in_variables[3], args=in_variables[4])
