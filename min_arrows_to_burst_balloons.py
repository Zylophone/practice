class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 2:
            return len(points)
        points = sorted(points, key=lambda p: p[1])
        end = points[0][0] - 1
        overlapped = 0
        for point in points:
            if end >= point[0]:
                overlapped += 1
            else:
                end = point[1]
        return len(points) - overlapped


print Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])
