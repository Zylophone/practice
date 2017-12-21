import heapq


class Solution(object):
    def scheduleCourse(self, A):
        pg = []
        start = 0
        for t, end in sorted(A, key=lambda (t, end): end):
            start += t
            heapq.heappush(pg, -t)
            if start > end:
                start += heapq.heappop(pg)
        return len(pg)

print Solution().scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])
