def find_peaksVH(arr1d):
    from scipy.signal import find_peaks
    peaks = find_peaks(arr1d, height=30)
    if len(peaks[0]) >= 3:
        return 3
    if len(peaks[0]) >= 2:
        return 2
    if len(peaks[0]) >= 1:
        return 1
    if len(peaks[0]) < 1:
        return 0


def find_peaksVV(arr1d):
    from scipy.signal import find_peaks
    peaks = find_peaks(arr1d, height=25)
    if len(peaks[0]) >= 3:
        return 3
    if len(peaks[0]) >= 2:
        return 2
    if len(peaks[0]) >= 1:
        return 1
    if len(peaks[0]) < 1:
        return 0
