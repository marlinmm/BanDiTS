import numpy as np
import pathos.multiprocessing as mp
from pathos import multiprocessing
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
#arr = io.imread("C:/Users/jz199/Desktop/S1A_VH_Agulhas_50m_selected_bands_VH_subset.tif")

chunks = [(sub_arr)
          for sub_arr in np.array_split(arr, mp.cpu_count())]

"""
def take_z_values():
    chunks = [(sub_arr)
          for sub_arr in np.array_split(arr, mp.cpu_count())]

    pool = multiprocessing.Pool()
    individual_results = pool.map(unpacking_apply_along_axis, chunks)
    # Freeing the workers:
    pool.close()
    pool.join()

    return np.concatenate(individual_results)
"""
#Call chunks individually through n-1
print(chunks)
print(len(chunks))

print(chunks[0].shape)
"""
print(chunks[1].shape)
print(chunks[2].shape)
print(chunks[3].shape)
print(chunks[4].shape)
print(chunks[5].shape)
print(chunks[6].shape)
print(chunks[7].shape)
print(chunks[8].shape)
print(chunks[9].shape)
print(chunks[10].shape)
print(chunks[11].shape)
"""

print(sum([chunk.shape[0] for chunk in chunks]))


