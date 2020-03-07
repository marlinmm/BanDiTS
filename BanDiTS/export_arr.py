import rasterio as rio


def functions_out_array(outname, arr, input_file, dtype):
    """
    this function is used to export the numpy array to a georeferenced datatype that is equal to the input datatype
    ----------
    outname: string
        combined name of the output folder and file of the raster file
    arr: numpy.array
        the calculated array following the execution of the applied functions to the input array
    input_file: string
         combined name of the input folder and file, so the function knows the used file format
    dtype: type
        is used to update the datatype of the dataset according to the used datatype. float64 is reduced to float32
        in some functions to save disk storage

    Returns
    ----------
    function has no return value
    """
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
