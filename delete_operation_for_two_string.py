class Solution(object):
    def minDistance(self, word1, word2):

        dp = [[10000 for _ in xrange(0, len(word2) + 1)] for _ in xrange(0, len(word1) + 1)]
        for i in xrange(0, len(word1) + 1):
            for j in xrange(0, len(word2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[len(word1)][len(word2)]

s = Solution()
print s.minDistance('eat', 'cat')