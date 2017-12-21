import sys


def find_median(nums):
    n = len(nums)
    start, end = -sys.maxint - 1, sys.maxint
    if n % 2 == 0:
        return float(find_k(nums, n / 2 - 1, start, end) + find_k(nums, n / 2, start, end)) / 2
    else:
        return find_k(nums, n / 2, start, end)


def find_k(nums, k, start, end):
    if start >= end:
        return start

    mid = start + (end - start) / 2
    cnt = 0
    for n in nums:
        if n < mid:
            cnt += 1
    if cnt == k:
        return mid
    elif cnt < k:
        start = mid + 1
    else:
        end = mid
    return find_k(nums, k, start, end)


print find_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
