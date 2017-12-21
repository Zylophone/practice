class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1
        i = 0
        add = 0
        while miss <= n:
            if len(nums) > i and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                add += 1
                miss += miss
        return add

print Solution().minPatches([2, 3], 4)
