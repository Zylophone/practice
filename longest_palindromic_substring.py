class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        if n < 2:
            return s
        result = s[0]

        dp = [[False for x in range(n)] for y in range(n)]

        for i in range(0, n):
            dp[i][i] = True

        for l in range(1, n):
            for i in range(0, n):
                if i + l >= n:
                    break
                if l == 1:
                    dp[i][i + l] = s[i] == s[i + l]
                else:
                    dp[i][i + l] = s[i] == s[i + l] and dp[i + 1][i + l - 1]
                if dp[i][i + l]:
                    result = s[i: i + l + 1]
        return result

s = Solution()
print s.longestPalindrome('dbbd')