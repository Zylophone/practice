import sys


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        if not m:
            return 1
        n = len(dungeon[0])
        if not n:
            return 1
        dp = [sys.maxint] * (n + 1)
        dp[n - 1] = 1
        for i in xrange(m - 1, -1, -1):
            for j in xrange(n - 1, -1, -1):
                hp = min(dp[j], dp[j + 1]) - dungeon[i][j]
                if hp <= 0:
                    hp = 1
                dp[j] = hp
        return dp[0]


print Solution().calculateMinimumHP([[-3], [-7]])
