import rasterio as rio
import rasterio.mask

def raster_mask_func(raster, shape, output_folder):
    out_image, out_transform = rio.mask.mask(raster, shape, crop=True)
    out_meta = raster.meta

    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform})
    print(out_image)
    #out_meta['nodata'] = None
    #return out_image
    #with rio.open(output_folder + "masked.tif", "w", **out_meta) as dest:
        #dest.write(out_image)