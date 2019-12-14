# Python Program illustrating
# apply_along_axis() in NumPy

import numpy as geek
from datetime import datetime

start_time = datetime.now()

# 1D_func is "geek_fun"
def geek_fun(a):
    # Returning the sum of elements at start index and at last index
    # inout array
    return (a[-1])


arr = geek.array([[1, 4, 5],
                  [6, 2, 8],
                  [9, 3, 5]])

print("axis=0 : ", geek.apply_along_axis(geek_fun, 0, arr))
print("\n")

print("axis=1 : ", geek.apply_along_axis(geek_fun, 1, arr))

end_time = datetime.now()
print(end_time-start_time, "seconds")

