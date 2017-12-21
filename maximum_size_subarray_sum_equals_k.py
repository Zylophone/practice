#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)


def maxSubArrayLen(nums, k):
    max_length = 0
    m = {0: -1}
    sum = 0
    for i, num in enumerate(nums):
        sum += num
        if sum not in m:
            m[sum] = i
        diff = sum - k
        if diff in m:
            max_length = max(max_length, i - m[diff])
    return max_length


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s, %(name)s %(levelname)s %(message)s',
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO)
    print maxSubArrayLen([1, -1, 5, -2, 3], 3)
