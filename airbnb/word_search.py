class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        visit = [[False for _ in xrange(n)] for _ in xrange(m)]

        def dfs(x, y, suffix):
            if not suffix:
                return True
            if 0 <= x < m and 0 <= y < n and not visit[x][y] and suffix[0] == board[x][y]:
                visit[x][y] = True
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if dfs(x + dx, y + dy, suffix[1:]):
                        return True
                visit[x][y] = False
            return False

        for i in xrange(m):
            for j in xrange(n):
                if dfs(i, j, word):
                    return True
        return False

