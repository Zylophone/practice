class Solution(object):
    def less_than(self, nums, target):
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start


    def greater_than(self, nums, target):
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) / 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid
        return start

print Solution().less_than([1,3,5,7,9], 6)
print Solution().greater_than([1,3,5,6,6,6,7,9], 6)
import bisect
#bisect.bisect_left()
