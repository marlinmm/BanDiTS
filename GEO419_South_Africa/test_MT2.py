import numpy as np
import pathos.multiprocessing as mp
from skimage import io
import sys
from functools import reduce
"""
###Example explanation with indexing:
Ni, Nk = a.shape[:axis], a.shape[axis+1:]
Nj = indices.shape
for ii in ndindex(Ni):
    for jj in ndindex(Nj):
        for kk in ndindex(Nk):
            out[ii + jj + kk] = a[ii + (indices[jj],) + kk]
"""


np.set_printoptions(threshold=sys.maxsize)

arr = io.imread("C:/Users/marli/Desktop/GEO402_Testdaten/S1A_VH_Agulhas_50m_selected_bands_VH_subset.tif")
#arr = io.imread("C:/Users/jz199/Desktop/S1A_VH_Agulhas_50m_selected_bands_VH.tif")

chunks = [(sub_arr)
          for sub_arr in np.array_split(arr, mp.cpu_count())]

def take_z_values():
    chunks = [(sub_arr)
          for sub_arr in np.array_split(arr, mp.cpu_count())]

    pool = multiprocessing.Pool()
    individual_results = pool.map(unpacking_apply_along_axis, chunks)
    # Freeing the workers:
    pool.close()
    pool.join()

    return np.concatenate(individual_results)



print(len(chunks))
print(chunks[13].shape)

print(sum([chunk.shape[0] for chunk in chunks]))


