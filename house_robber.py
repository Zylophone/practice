class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            tmp = now
            now = max(now, last + i)
            last = tmp
        return now


print Solution().rob([1, 3, 1])
