class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        result = sorted(envelopes, cmp=lambda x, y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        size = 0
        tails = [0] * len(envelopes)
        for env in result:
            start, end = 0, size
            while start != end:
                mid = (start + end) / 2
                if tails[mid] < env[1]:
                    start = mid + 1
                else:
                    end = mid
            tails[start] = env[1]
            size = max(start + 1, size)
        return size


print Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]])
