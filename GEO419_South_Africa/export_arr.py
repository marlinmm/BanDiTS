import rasterio as rio


def out_array(outname, arr, input_file, dtype):
    with rio.open(input_file) as src:
        ras_meta = src.profile
        corr_count = {'count': 1}
        ras_meta.update(corr_count)

    # make any necessary changes to raster properties, e.g.:
    ras_meta['dtype'] = dtype
    #ras_meta['nodata'] = -99

    with rio.open(outname, 'w', **ras_meta) as dst:
        dst.write(arr, 1)