import fiona
import rasterio
import rasterio.mask
from GEO419_South_Africa import export_arr


def mask_raster_test(outname):
    with fiona.open("C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Shapes/fire_feb_2017_subset_reproj.shp", "r") as shapefile:
        shapes = [feature["geometry"] for feature in shapefile]
    for i in range(0, len(shapes)):
        with rasterio.open("C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/S1A_VH_Agulhas_50m_selected_bands_VH_subset2.tif") as src:
            out_image, out_transform = rasterio.mask.mask(src, [shapes[i]], crop=True)
            # out_meta = src.meta
            export_arr.out_array(outname=outname + i, arr=out_image, input_file="C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/S1A_VH_Agulhas_50m_selected_bands_VH_subset2.tif", dtype="float32")
    #return out_image