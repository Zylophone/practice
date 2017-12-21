class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        def dfs(x, y):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    if not dp[nx][ny]:
                        dp[nx][ny] = dfs(nx, ny)
                    dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
            dp[x][y] = max(dp[x][y], 1)
            return dp[x][y]

        for x in range(m):
            for y in range(n):
                if not dp[x][y]:
                    dp[x][y] = dfs(x, y)
        return max([max(x) for x in dp])


print Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
