class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = len(heightMap)
        n = len(heightMap[0])

        peakMap = [[1e9] * n for _ in range(m)]
        a = []
        for x in range(m):
            for y in range(n):
                if x in (0, m - 1) or y in (0, n - 1):
                    peakMap[x][y] = heightMap[x][y]
                    a.append((x, y))

        while a:
            x, y = a.pop(0)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = dx + x, dy + y
                if not 0 <= nx < m or not 0 <= ny < n:
                    continue
                limit = max(peakMap[x][y], heightMap[nx][ny])
                if peakMap[nx][ny] > limit:
                    peakMap[nx][ny] = limit
                    a.append((nx, ny))

        return sum(peakMap[x][y] - heightMap[x][y] for x in range(m) for y in range(n))

