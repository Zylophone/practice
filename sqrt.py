class Solution(object):
    def sqrt(self, n):
        start, end = 1, n / 2
        while start < end:
            mid = (start + end) / 2
            res = mid * mid
            if res == n:
                return mid
            elif res > n:
                end = mid - 1
            else:
                start = mid + 1
        return start if start * start <= n else start - 1


print Solution().sqrt(80)
