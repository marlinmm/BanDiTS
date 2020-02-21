# BanDiTS (Breakpoint Detection in Timeseries for Sentinel-1)

### This tool aims to make detecting breakpoints and anomalies in Sentinel-1 time series easier:
This package is a project by Marlin M. Mueller and Jonas Ziemer for the module GEO419 of the M.Sc. Geoinformatics at the Friedrich-Schiller-University Jena. 
It provides a framework for importing 3D-raster files in _rasterio_-compatible formats and provides basic filtering and statistical functionality. 
It was developed mainly for fire and agricultural breakpoint detection

Basic functionality includes:

* Importing time series data and preliminary light cleaning of data (specifically developed for Sentinel-1 stacks created in ENVI, but should work with all kinds of time series stacks)
* applying different statistical functions along time axis of data to retrieve different metrics on a time scale
* applying different filter functions along time axis of data to enable better detection of breakpoints
* creating new raster files to visualize applied functions
* working in parallelized, multithreaded way for efficient computation _(6x faster with 16 threads vs 1 thread)_
    * 2n RAM-usage
* easy expansion with new functions is possible

_developed in Python 3.8_

# Installation
In case you have git installed you can install the package as follows:

    pip install git+https://github.com/marlinmm/BanDiTS.git

# _WORK IN PROGRESS_