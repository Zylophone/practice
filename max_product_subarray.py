class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        if not nums:
            return 0
        small, large = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                small, large = large, small

            large = max(large * nums[i], nums[i])
            small = min(small * nums[i], nums[i])

            res = max(res, large)
        return res


print Solution().maxProduct([2, -3, 2])
