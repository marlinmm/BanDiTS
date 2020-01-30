import fiona
import rasterio as rio
import rasterio.mask
from GEO419_South_Africa import export_arr


def mask_raster_test(outname):
    shapefile = fiona.open("C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Shapes/fire_feb_2017_subset_reproj.shp", "r")
    shapes = [feature["geometry"] for feature in shapefile]
    for i in range(0, len(shapes)):
        with rio.open("C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/S1A_VH_Agulhas_50m_selected_bands_VH_subset2.tif") as src:
            out_image, out_transform = rasterio.mask.mask(src, [shapes[i]], crop=True)
            ras_meta = src.profile
            ras_meta.update({"driver": "GTiff",
                             "height": out_image.shape[1],
                             "width": out_image.shape[2],
                             "transform": out_transform})
            # export_arr.out_array(outname=outname + i, arr=out_image, input_file="C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/Raster/S1A_VH_Agulhas_50m_selected_bands_VH_subset2.tif", dtype="float32")
            with rio.open(outname, 'w', **ras_meta) as dst:
                dst.write(out_image, 1)
    #return out_image