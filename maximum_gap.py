import math


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n < 2:
            return 0
        num_max = max(nums)
        num_min = min(nums)
        gap = int(math.ceil(float(num_max - num_min) / (n - 1)))

        if gap == 0:
            return 0
        bucket_len = (num_max - num_min) / gap + 1
        buckets = [None] * bucket_len
        for num in nums:
            idx = int((num - num_min) / gap)
            bucket = buckets[idx]
            if not bucket:
                buckets[idx] = {'min': num, 'max': num}
            else:
                buckets[idx] = {'min': min(num, bucket['min']), 'max': max(num, bucket['max'])}
        max_gap = 0
        i = 0
        while i < len(buckets):
            if not buckets[i]:
                i += 1
                continue

            j = i + 1
            while j < len(buckets) and not buckets[j]:
                j += 1
            if j < len(buckets):
                max_gap = max(max_gap, buckets[j]['min'] - buckets[i]['max'])
            i = j
        return max_gap


print Solution().maximumGap([1, 100])
