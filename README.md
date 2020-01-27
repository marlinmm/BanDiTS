# **Project for course GEO419 at FSU Jena**

### This tool aims to make detecting breakpoints and anomalies in Sentinel-1 time series easier:

* Importing time series data and preliminary light cleaning of data (specifically developed for Sentinel-1 stacks created in ENVI, but should work with all kinds of time series stacks)
* applying different functions along time axis of data to retrieve different metrics on a time scale
* giving user choice, which functions should be applied or used (planned)
* creating new raster files to visualize applied functions
* working in parallelized, multithreaded way _(6x faster with 16 threads vs 1 thread)_

_developed in Python 3.8_


# _WORK IN PROGRESS_