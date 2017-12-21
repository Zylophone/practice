class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if t == '':
            return 1
        if s == '':
            return 0

        dp = [[0 for _ in xrange(len(s) + 1)] for _ in xrange(len(t) + 1)]
        for j in range(0, len(s) + 1):
            dp[0][j] = 1

        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[len(t)][len(s)]


s = Solution()
print s.numDistinct('ddd', 'dd')
