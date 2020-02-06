from GEO419_South_Africa import preprocessing, apply_along_axis, export_arr, function, filter_functions
from pathos import multiprocessing as mp
from datetime import datetime
import numpy as np

start_time = datetime.now()

def main():

    ###################################     INPUT    ########################################

    # Input Folder Marlin:
    raster_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/"
    # Input Folder Jonas:
    # raster_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester\Vorlesungsmitschriften/GEO402 - Ableitung von Landoberflächenparametern/Subset/"

    # Input file name
    raster_filename = "S1_A_VH_agulhas_full_study_site_50m"
    # raster_filename = "SubsetVH.tif"

    ###################################     OUTPUT    ########################################

    # Output Folder Marlin:
    output_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/"
    # Output Folder Jonas:
    # output_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester\Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Output/"

    # Output File Name:
    output_file = raster_filename[0:len(raster_filename)-4] + "_median_filtered3.tif"
#simple_edge_detection
    ######################   NO USER INPUT BEYOND THIS POINT   ###############################

    input_raster = raster_folder + raster_filename
    outname = output_folder + output_file

    # arr: full size numpy array 3D XxYxZ 200x300x100
    arr = preprocessing.rio_array(input_raster)

    # creating filtered array depending on set filter function
    filtered_arr = apply_along_axis.parallel_apply_along_axis(func1d=filter_functions.median_filter5, arr=arr, axis=0, cores=mp.cpu_count())
    filtered_arr = np.rollaxis(filtered_arr, 2)
    filtered_arr = np.rollaxis(filtered_arr, 1)
    filtered_arr = np.rollaxis(filtered_arr, 2)
    dtype = type(filtered_arr[0][0][0])
    #print(type(dtype)
    #if type(dtype) == np.float64:
    #    print("lalala")
    # --> change float64 to float32

    export_arr.functions_out_array(outname=outname, arr=filtered_arr, input_file=input_raster, dtype=dtype)


    # creating results with calling wanted algorithm in parallel_apply_along_axis for quick runtime
    # result = apply_along_axis.parallel_apply_along_axis(func1d=function.combined_time, arr=arr, axis=0, cores=mp.cpu_count())

    # selecting dtype based on result
    # dtype = type(result[0][0])
    # dtype = type(filtered_arr[0][0])
    # float64 to float32

    # exporting result to new raster
    # export_arr.functions_out_array(outname=outname, arr=result, input_file=input_raster, dtype=dtype)
    # export_arr.functions_out_array(outname=outname, arr=filtered_arr, input_file=input_raster, dtype=dtype)

    end_time = datetime.now()
    print("end-time = ", end_time-start_time, "Hr:min:sec")

# main func
if __name__ == '__main__':
    main()
