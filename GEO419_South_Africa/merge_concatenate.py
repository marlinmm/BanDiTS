#import os
from GEO419_South_Africa import preprocessing, apply_along_axis, export_arr, function, mask_raster, tes_local_2
from pathos import multiprocessing as mp
from datetime import datetime

start_time = datetime.now()

def main():
    # # Input Folder Marlin:
    # raster_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/"
    # shape_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Shapes/"
    # # Input Folder Jonas:
    # # raster_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Testdaten/"
    #
    # # Input file name
    # raster_filename = "S1A_VH_Agulhas_50m_selected_bands_VH_subset2.tif"
    # shape_filename = "fire_feb_2017_subset_reproj.shp"
    #
    #
    # # Output Folder Marlin:
    # output_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/"
    # # Output Folder Jonas:
    # #output_folder = ""
    #
    # # Output File Name:
    # output_file = raster_filename + "_mask_test_test1.tif"
    #
    # ######################   NO USER INPUT BEYOND THIS POINT   ###############################


    ###################################     INPUT    ########################################

    # Input Folder Marlin:
    raster_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/"
    shape_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Shapes/"
    # Input Folder Jonas:
    # raster_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester\Vorlesungsmitschriften/GEO402 - Ableitung von Landoberflächenparametern/Subset/"

    # Input file name
    raster_filename = "S1A_VH_Agulhas_50m_selected_bands_VH_subset2.tif"
    #raster_filename = "SubsetVH.tif"
    # shape_filename = "threshold_VH.shp"

    ###################################     OUTPUT    ########################################

    # Output Folder Marlin:
    output_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/"
    # Output Folder Jonas:
    # output_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester\Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Output/"

    # Output File Name:
    output_file = raster_filename + "_combined_VH_2.tif"

    ######################   NO USER INPUT BEYOND THIS POINT   ###############################

    # example of changeble output names
        # basename = 'out{}.tif'
        # tuning = 3
        # outname = os.path.join(raster_folder, basename.format(tuning))

    # example of new sub directory creation
        # subdir = os.path.join(raster_folder, 'sub')
        # os.makedirs(subdir, exist_ok=True)

    input_raster = raster_folder + raster_filename
    input_shape = shape_folder + shape_filename
    outname = output_folder + output_file

    # arr: full size numpy array 3D XxYxZ 200x300x100
    arr = preprocessing.rio_array(input_raster)
    shp = preprocessing.fiona_shape(shape_path = input_shape)
    shapes = [feature["geometry"] for feature in shp]
    shapes1 = [shapes[0]]
    print(shapes1)
    print(shapes[0])
    print(type(shapes1))
    print(type(shapes[0]))


    #print(shp)
    #print(next(shp))
    #print(shp[0])
    #print(shp[1])

    #burn_dates = preprocessing.fiona_burn_date(input_shape)
    #print(burn_dates)


    #time_series_length = arr.shape[0]
    #print(time_series_length)

    #mask_raster.raster_mask_func(raster=input_raster, shape=shapes, output_folder=output_folder)

    result = tes_local_2.mask_raster_test(outname)
    export_arr.out_array(outname=outname, arr=result, input_file=input_raster, dtype="float32")

    #result = apply_along_axis.parallel_apply_along_axis(func1d=function.stdev, arr=arr, axis=0, cores=mp.cpu_count())
    #export_arr.out_array(outname=outname, arr=result, input_file = input_raster, dtype="float32")
    ### maybe add function wich checks used func1d and chosen dtype and lets you know before programm runs

### catch error of files dtype: ValueError: the array's dtype 'float32' does not match the file's dtype 'int32'  ####

    end_time = datetime.now()
    print("end-time = ", end_time-start_time, "Hr:min:sec")

# main func
if __name__ == '__main__':
    main()
