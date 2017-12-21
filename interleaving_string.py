class Solution():
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        dp = [[False for i in xrange(len(s2) + 1)] for k in xrange(len(s1) + 1)]
        for i in xrange(0, len(s1) + 1):
            for j in xrange(0, len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i - 1]
                else:
                    dp[i][j] = (dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]) or (dp[i][j - 1] and s3[i + j - 1] == s2[j - 1])
        return dp[len(s1)][len(s2)]


s = Solution()

print s.isInterleave('123', '234', '123234')
