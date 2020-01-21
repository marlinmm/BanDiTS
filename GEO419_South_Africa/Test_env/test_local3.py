from multiprocessing import Pool, TimeoutError
import time
import os
import sys
import os
from datetime import datetime
import numpy as np
import pathos.multiprocessing as mp
from pathos import multiprocessing
from multiprocessing import Process
from skimage import io
import pylab as plt

def f(x):
    return x*x
#
if __name__ == '__main__':
    pool = multiprocessing.Pool(mp.cpu_count())            # start 4 worker processes

    # print "[0, 1, 4,..., 81]"
    print(pool.map(f, range(100000000)))