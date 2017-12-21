class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k > len(prices)/2:
            return self.quickSolve(prices)

        g = [[0 for _ in xrange(0, k + 1)] for _ in xrange(0, len(prices))]
        l = [[0 for _ in xrange(0, k + 1)] for _ in xrange(0, len(prices))]

        for i in range(0, len(g)):
            for j in range()


    def quickSolve(self, prices):
        s = 0
        for i in range(1, len(prices)):
            s += max(prices[i] - prices[i - 1], 0)
        return s
