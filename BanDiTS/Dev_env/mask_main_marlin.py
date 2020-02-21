#import os
from BanDiTS import preprocessing, export_arr
from datetime import datetime

start_time = datetime.now()

def main():
    ###################################     INPUT    ########################################

    # Input Folder Marlin:
    raster_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/"
    #shape_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Shapes/"
    # Input Folder Jonas:
    # raster_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester\Vorlesungsmitschriften/GEO402 - Ableitung von Landoberflächenparametern/Subset/"

    # Input file name
    raster_filename = "S1_A_VH_agulhas_full_study_site_50m"
    #raster_filename = "SubsetVH.tif"
    # shape_filename = "threshold_VH.shp"

    ###################################     OUTPUT    ########################################

    # Output Folder Marlin:
    output_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/"
    # Output Folder Jonas:
    # output_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester\Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Output/"

    # Output File Name:
    output_file = raster_filename + "cleaned.tif"

    ######################   NO USER INPUT BEYOND THIS POINT   ###############################

    input_raster = raster_folder + raster_filename
    #input_shape = shape_folder + shape_filename
    outname = output_folder + output_file

    # arr: full size numpy array 3D XxYxZ 200x300x100
    arr = preprocessing.rio_array(input_raster)
    #shp = preprocessing.fiona_shape(shape_path = input_shape)
    #shapes = [feature["geometry"] for feature in shp]
    #shapes1 = [shapes[0]]

    #burn_dates = preprocessing.fiona_burn_date(input_shape)
    #print(burn_dates)


    #time_series_length = arr.shape[0]
    #print(time_series_length)

    #mask_raster.raster_mask_func(raster=input_raster, shape=shapes, output_folder=output_folder)

    #result = tes_local_2.mask_raster_test(outname)
    #export_arr.out_array(outname=outname, arr=result, input_file=input_raster, dtype="float32")

    #result = apply_along_axis.parallel_apply_along_axis(func1d=function.slope_minimum, arr=arr, axis=0, cores=mp.cpu_count())
    result = arr
    #dtype = type(result[0][0])
    export_arr.cleaned_out_array(outname=outname, arr=result, input_file=input_raster, dtype="float32")

    end_time = datetime.now()
    print("end-time = ", end_time-start_time, "Hr:min:sec")

# main func
if __name__ == '__main__':
    main()
