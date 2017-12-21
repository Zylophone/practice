class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l + r) / 2

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

