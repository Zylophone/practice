class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not len(grid) or not len(grid[0]):
            return 0
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = '2'
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count


print Solution().numIslands([list("1011011")])
