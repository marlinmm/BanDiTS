import fiona
import rasterio as rio
import rasterio.mask
import numpy as np
import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

list_list = []


def mask_raster_test():
    import numpy as np
    shape_list = []
    for h in range(1,9):
        shapefile = fiona.open("C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Shapes/A_test_export_polygon_reproj" + str(h) + ".shp", "r")
        shapes = [feature["geometry"] for feature in shapefile]
        shape_list.append(shapes)
    #print(len(shape_list))
    #print(shape_list)
    #print(shape_list[0])
    #print(shape_list[1][0])

    for i in range(0, len(shape_list)):
        src1 = rio.open("C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/Original/S1A_VH_Agulhas_50m_selected_bands_VH_2.tif")
        src2 = rio.open("C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/S1_A_VV_agulhas_full_median_filtered11_sobel9.tif")
        out_image1, out_transform1 = rasterio.mask.mask(src1, [shape_list[i][0]], crop=True, nodata= np.nan)
        out_image2, out_transform2 = rasterio.mask.mask(src2, [shape_list[i][0]], crop=True, nodata=np.nan)
        ras_meta1 = src1.profile
        ras_meta2 = src2.profile
        ras_meta1.update({"driver": "GTiff",
                         "height": out_image1.shape[1],
                         "width": out_image1.shape[2],
                         "transform": out_transform1,
                         "nodata": 0. })
        ras_meta2.update({"driver": "GTiff",
                         "height": out_image1.shape[1],
                         "width": out_image1.shape[2],
                         "transform": out_transform2,
                         "nodata": 0. })
        list1 = []
        for j in range(0, len(out_image1)):
            tmp = np.nanmean(out_image1[j])
            list1.append(tmp)

        list2 = []
        for k in range(0, len(out_image2)):
            tmp2 = np.nanmean(out_image2[k])
            list2.append(tmp2)
        list2_clean = np.delete(list2, [79, 81, 83, 85, 87, 89, 92, 94, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 130, 132], 0)
        med_filter1 = sig.medfilt(list1, kernel_size=11)

        kernel = [-5, -5, -5, -5, 0, 5, 5, 5, 5]
        # kernel = [-5, 0, 5]
        out = np.float32(np.convolve(med_filter1, kernel, "valid"))


        from scipy.signal import find_peaks
        peaks = find_peaks(out, height=10, distance=10)
        print(peaks[0][0])

        median_value = np.median(out)
        mean_value = np.mean(out)

        original_VH = list1
        median_filter_VH = med_filter1
        sobel_filter_VH = out
        sobel_filter_VV = list2_clean

        #data4 = [median_value] * len(sobel_filter)
        #data5 = [mean_value] * len(sobel_filter)

        fig, ax1 = plt.subplots()

        # color = '#bebebe'
        #plt.title('Edge Detection (VH vs. VV ' + str(i+1) + ')')
        ax1.set_xlabel('No. of values')
        # ax1.plot(original_VH, color=color, linewidth=1)
        #
        # color = 'tab:red'
        # ax1.set_ylabel('median', color=color)  # we already handled the x-label with ax1
        # ax1.plot(median_filter_VH, color=color)
        # ax1.tick_params(axis='y', labelcolor=color)
        #
        # ax3 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        #
        # color = 'tab:green'
        # ax3.set_ylabel('Edge detection', color=color)  # we already handled the x-label with ax1
        # ax3.plot(sobel_filter_VH, color=color)
        # ax3.tick_params(axis='y', labelcolor=color)

        # color = '#bebebe'
        # ax1.set_xlabel('no. of values')
        # ax1.plot(original_VH, color=color, linewidth=1)
        plt.ylim(-30, 60)
        color = 'tab:green'
        ax1.set_ylabel('Edge Detection VH', color=color)  # we already handled the x-label with ax1
        ax1.plot(sobel_filter_VH, color=color)
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        plt.ylim(-30, 60)
        color = 'tab:red'
        ax2.set_ylabel('Edge Detection VV', color=color)  # we already handled the x-label with ax1
        ax2.plot(sobel_filter_VV, color=color)
        ax2.tick_params(axis='y', labelcolor=color)

        #color = 'tab:blue'
        #ax3.plot(data4, color=color)

        #color = '#ffff00'
        #ax3.plot(data5, color=color)

        fig.tight_layout()  # otherwise the right y-label is slightly clipped

        plt.show()

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
#mask_raster_test()