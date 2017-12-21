import heapq


class Solution(object):
    def smallestRange1(self, A):
        q = [(row[0], i, 0) for i, row in enumerate(A)]
        heapq.heapify(q)
        ans = 1e-9, 1e9
        right = max(n for n, _, _ in q)
        while True:
            left, i, j = heapq.heappop(q)
            if right - left < ans[1] - ans[0]:
                ans = left, right

            if len(A[i]) == j + 1:
                return ans

            v = A[i][j + 1]
            right = max(v, right)
            heapq.heappush(q, (v, i, j + 1))

    def smallestRange(self, A):
        q = []
        for row in A:
            q.append((row[0], row))
        heapq.heapify(q)
        ans = 1e-9, 1e9
        right = max([first_num for first_num, row in q])
        while True:
            left, row = heapq.heappop(q)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if not row:
                return ans

            v = row[0]
            right = max(v, right)
            heapq.heappush(q, (v, row[1:]))



print Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
