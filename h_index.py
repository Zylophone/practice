class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        if n == 0:
            return 0

        count = [0] * n
        for i in citations:
            if i > n:
                i = n
            if i == 0:
                continue
            count[i - 1] += 1
        s = 0
        for i in range(n - 1, -1, -1):
            s += count[i]
            if s > i:
                return i + 1
        return 0


print Solution().hIndex([100])
