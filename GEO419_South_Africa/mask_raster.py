import fiona
import rasterio as rio
import rasterio.mask
import csv
import matplotlib.pyplot as plt
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
    shapefile = fiona.open("C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Shapes/2018_merge_clipped_reproj.shp", "r")
    shapes = [feature["geometry"] for feature in shapefile]

    for i in range(0, len(shapes)):
        src = rio.open("C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/S1_A_VH_agulhas_full_study_site_50mcleaned.tif")
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
        plt.plot(list1)
        plt.show()




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