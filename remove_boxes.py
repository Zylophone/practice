class Solution(object):
    """
    dfs timeout
    def removeBoxes(self, boxes):
        result = [0]
        self.run(boxes, 0, result)
        return result[0]

    def run(self, boxes, sum, result):
        if not boxes:
            result[0] = max(result[0], sum)
            return
        for i in xrange(0, len(boxes)):
            k = i + 1
            while k < len(boxes) and boxes[k] == boxes[i]:
                k += 1
            new_boxes = boxes[:i] + boxes[k:]
            self.run(new_boxes, sum + (k - i) * (k - i), result)
    """

    def removeBoxes(self, boxes):
        n = len(boxes)
        dp = [[[0] * n] * n] * n
        return self.helper(boxes, 0, n - 1, 0, dp)

    def helper(self, boxes, i, j, k, dp):
        if i > j:
            return 0
        if dp[i][j][k] > 0:
            return dp[i][j][k]
        res = (k + 1) * (k + 1) + self.helper(boxes, i + 1, j, 0, dp)
        for m in range(i + 1, j + 1):
            if boxes[i] == boxes[m]:
                res = max(res, self.helper(boxes, i + 1, m - 1, 0, dp) + self.helper(boxes, m, j, k + 1, dp))
        dp[i][j][k] = res
        return res


s = Solution()
print s.removeBoxes([2, 3, 2])
