from GEO419_South_Africa import preprocessing, apply_along_axis, export_arr, function, mask_raster
from pathos import multiprocessing as mp
from datetime import datetime

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
    output_file = raster_filename + "_slope_slope_min.tif"
    ######################   NO USER INPUT BEYOND THIS POINT   ###############################


    input_raster = raster_folder + raster_filename
    outname = output_folder + output_file

    # arr: full size numpy array 3D XxYxZ 200x300x100
    arr = preprocessing.rio_array(input_raster)

    # crating results with calling wnated algorithm in parallel_apply_along_axis for quick runtime
    result = apply_along_axis.parallel_apply_along_axis(func1d=function.slope_minimum, arr=arr, axis=0, cores=mp.cpu_count())

    # selecting dtype based on result
    dtype = type(result[0][0])

    # exporting result to new raster
    export_arr.out_array(outname=outname, arr=result, input_file=input_raster, dtype=dtype)


    end_time = datetime.now()
    print("end-time = ", end_time-start_time, "Hr:min:sec")

# main func
if __name__ == '__main__':
    main()
