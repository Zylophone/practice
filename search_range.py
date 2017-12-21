import bisect
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        start = bisect.bisect_left(nums, target)
        if start >= len(target) or nums[start] != target:
            return [-1, -1]

        return [start, bisect.bisect_right(nums, target) - 1]


print Solution().searchRange([2, 2], 3)
