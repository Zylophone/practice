from math import *


def round_up(arr):
    float_sum = fsum(arr)
    rounded_sum = round(float_sum)
    floored_arr = map(int, map(floor, arr))
    floored_sum = fsum(floored_arr)
    diff_mapping = {}
    for i in range(len(arr)):
        diff_mapping[i] = arr[i] - floored_arr[i]
    sorted_diff = sorted(diff_mapping.iteritems(), key=lambda d: d[1], reverse=True)
    diff_sum = int(rounded_sum - floored_sum)

    for i in range(diff_sum):
        idx, diff = sorted_diff[i]
        floored_arr[idx] += 1
    return floored_arr

print round_up([1.2, 2.3, 3.4])
