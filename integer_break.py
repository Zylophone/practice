class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [None] * (n + 1)
        for i in range(1, n + 1):
            if i == 1:
                dp[i] = 0
                continue
            tmp = i - 1
            for k in range(1, i / 2 + 1):
                tmp = max(tmp, dp[k] * dp[i - k])
            dp[i] = tmp

        return dp[n]


print Solution().integerBreak(10)
