class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = 0
        left_most = [0] * len(height)
        right_most = [0] * len(height)
        for i in range(0, len(height)):
            if i == 0:
                continue
            left_most[i] = max(left_most[i - 1], height[i - 1])

        for i in range(0, len(height))[::-1]:
            if i == len(height) - 1:
                continue
            right_most[i] = max(right_most[i + 1], height[i + 1])

        for i in range(0, len(height)):
            h = min(left_most[i], right_most[i]) - height[i]
            if h < 0:
                h = 0
            s += h

        return s


print Solution().trap([2, 0, 2])
