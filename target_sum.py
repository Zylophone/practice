import collections


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = collections.Counter()
        dp[0] = 1
        for num in nums:
            ndp = collections.Counter()
            for key in dp.keys():
                ndp[key - num] += dp[key]
                ndp[key + num] += dp[key]
            dp = ndp
        return dp[S]





print Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)
