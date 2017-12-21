from math import *


def ip2int(s):
    items = s.split('.')
    val = 0
    for item in items:
        val = val * 256 + int(item)
    return val


def int2ip(num):
    item = [0] * 4
    i = 0
    while num > 0:
        item[i] = num % 256
        num /= 256
        i += 1
    return '.'.join(map(str, reversed(item)))


def range2cidr(start, end):
    if start == end:
        return [start + '/32']
    start, end = ip2int(start), ip2int(end)
    result = []
    while start <= end:
        first_one = start & -start
        mask_current = 32 - int(log(first_one, 2)) if first_one != 0 else 0
        mask_diff = 32 - int(log(end - start + 1, 2))
        mask_current = max(mask_current, mask_diff)
        result.append(int2ip(start) + '/' + str(mask_current))
        start += 2 ** (32 - mask_current)
    return result

# print ip2int('0.0.1.0')
# print int2ip(257)
print range2cidr('0.0.0.3', '0.159.159.159')
