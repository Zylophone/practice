class Solution(object):
    def hIndex(self, citations):
        if not citations:
            return 0

        start = 0
        end = len(citations) - 1

        while start <= end:
            mid = (start + end) / 2
            if citations[mid] >= len(citations) - mid:
                end = mid - 1
            else:
                start = mid + 1

        return len(citations) - start


print Solution().hIndex([2, 3, 4, 5, 6])
