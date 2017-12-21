class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [[0 for _ in range(0, n)] for _ in range(0, m)]
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] != '1':
                    continue

                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                res = max(dp[i][j], res)
        return res * res


print Solution().maximalSquare(["10100", "10111", "11111", "10010"])
