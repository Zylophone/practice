class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        i = 0
        m = 0
        s = []
        while i < len(heights):
            if not s or heights[i] > heights[s[-1]]:
                s.append(i)
                i += 1
            else:
                tmp = s.pop(-1)
                m = max(m, heights[tmp] * (i if not s else i - s[-1] - 1))
        return m


print Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
