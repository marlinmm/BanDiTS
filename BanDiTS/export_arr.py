import rasterio as rio


def functions_out_array(outname, arr, input_file, dtype):
    arr_shape = arr.shape
    tmp = arr_shape[0]
    if len(arr_shape) <= 2:
        with rio.open(input_file) as src:
            ras_meta = src.profile
            corr_count = {'count': 1}
            ras_meta.update(corr_count)

        # make any necessary changes to raster properties:
        ras_meta['dtype'] = dtype

        with rio.open(outname, 'w', **ras_meta) as dst:
            dst.write(arr, 1)
    else:
        with rio.open(input_file) as src:
            ras_meta = src.profile
            corr_count = {'count': tmp}
            ras_meta.update(corr_count)

        # make any necessary changes to raster properties:
        ras_meta['dtype'] = dtype

        with rio.open(outname, 'w', **ras_meta) as dst:
            dst.write(arr,)

