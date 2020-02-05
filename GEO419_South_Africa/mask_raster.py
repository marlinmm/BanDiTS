import fiona
import rasterio as rio
import rasterio.mask
import numpy as np
import csv
import matplotlib.pyplot as plt
import scipy.signal as sig
from GEO419_South_Africa import preprocessing
from GEO419_South_Africa import export_arr


# def mask_raster_test(outname):
#     shapefile = fiona.open("C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Shapes/fire_feb_2017_subset_reproj.shp", "r")
#     shapes = [feature["geometry"] for feature in shapefile]
#     for i in range(0, len(shapes)):
#         with rio.open("C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/S1A_VH_Agulhas_50m_selected_bands_VH_subset2.tif") as src:
#             out_image, out_transform = rasterio.mask.mask(src, [shapes[i]], crop=True)
#             ras_meta = src.profile
#             ras_meta.update({"driver": "GTiff",
#                              "height": out_image.shape[1],
#                              "width": out_image.shape[2],
#                              "transform": out_transform})
#             # export_arr.out_array(outname=outname + i, arr=out_image, input_file="C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/S1A_VH_Agulhas_50m_selected_bands_VH_subset2.tif", dtype="float32")
#             with rio.open(outname, 'w', **ras_meta) as dst:
#                 dst.write(out_image, 1)
#     #return out_image

list_list = []
def mask_raster_test():
    import numpy as np
    # shapefile = fiona.open("C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Shapes/pivot_test_reproj.shp", "r")
    shapefile = fiona.open("C:/Users/jz199/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Shapes/pivot.shp", "r")
    shapes = [feature["geometry"] for feature in shapefile]

    for i in range(0, len(shapes)):
        # src = rio.open("C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/S1_A_VH_agulhas_full_study_site_50mcleaned.tif")
        src = rio.open("C:/Users/jz199/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO402 - Ableitung von Landoberflächenparametern/Subset/SubsetVH.tif")
        out_image, out_transform = rasterio.mask.mask(src, [shapes[i]], crop=True, nodata= np.nan)
        ras_meta = src.profile
        ras_meta.update({"driver": "GTiff",
                         "height": out_image.shape[1],
                         "width": out_image.shape[2],
                         "transform": out_transform,
                         "nodata": 0. })


        list1 = []
        for j in range(0, len(out_image)):
            tmp = np.nanmean(out_image[j])
            list1.append(tmp)


        med_filter = sig.medfilt(list1, kernel_size=3)


        # kernel = [-5, -5, -5, -5, 0, 5, 5, 5, 5]
        kernel = [-5, -5, 0, 5, 5]
        #print(kernel)
        out = np.float32(np.convolve(med_filter, kernel, "valid"))


        from scipy.signal import find_peaks
        peaks = find_peaks(out, height=30)
        #print(peaks)
        print(peaks[0])
        #print(peaks[1])

        # median_value = np.median(out)
        # mean_value = np.mean(out)
        #
        # data1 = list1
        # data2 = med_filter
        # data3 = out
        # data4 = [median_value] * len(data3)
        # data5 = [mean_value] * len(data3)
        #
        #
        #
        # fig, ax1 = plt.subplots()
        #
        # color = '#bebebe'
        # ax1.set_xlabel('no. of values')
        # ax1.plot(data1, color=color, linewidth=1)
        #
        # color = 'tab:red'
        # ax1.set_ylabel('median', color=color)  # we already handled the x-label with ax1
        # ax1.plot(data2, color=color)
        # ax1.tick_params(axis='y', labelcolor=color)
        #
        # ax3 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        #
        # color = 'tab:green'
        # ax3.set_ylabel('Edge detection', color=color)  # we already handled the x-label with ax1
        # ax3.plot(data3, color=color)
        # ax3.tick_params(axis='y', labelcolor=color)
        #
        # color = 'tab:blue'
        # ax3.plot(data4, color=color)
        #
        # color = '#ffff00'
        # ax3.plot(data5, color=color)
        #
        # fig.tight_layout()  # otherwise the right y-label is slightly clipped
        # plt.show()

        # fig, ax1 = plt.subplots()
        # # plt.plot(out)
        # ax1.set_ylabel("db" + str(i))
        # plt.plot(list1)
        # plt.show()





        # with open("C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/test" + str(i) + ".txt", 'w', newline='') as myfile:
        #     #wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        #     wr = csv.writer(myfile, delimiter=',')
        #     wr.writerow(list1)

        #list_list.append(list1)
    #print(list_list)

        #with rio.open("C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/test.tif", 'w', **ras_meta) as dst:
        #    dst.write(out_image)

        # export_arr.out_array(outname=outname + i, arr=out_image, input_file="C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/S1A_VH_Agulhas_50m_selected_bands_VH_subset2.tif", dtype="float32")
        # with rio.open(outname, 'w', **ras_meta) as dst:
        #     dst.write(out_image, 1)
    #return out_image


#### activate for testing this file standalone ####
mask_raster_test()
