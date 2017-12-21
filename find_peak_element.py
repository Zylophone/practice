class Solution(object):
    def findPeak(self, nums):
        if len(nums) < 3:
            return -1
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            if mid == 0 or mid == len(nums) - 1:
                return -1

            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid] > nums[mid + 1]:
                end = mid - 1
            else:
                start = mid + 1
        return -1


print Solution().findPeak([1, 2, 3, 1])
