class Solution(object):
    def longestConsecutive(self, num):
        d = {}
        res = 0
        for n in num:
            if n in d:
                continue
            l, r = d.get(n - 1, 0), d.get(n + 1, 0)
            sum = l + r + 1
            d[n] = sum
            res = max(res, sum)
            d[n - l] = sum
            d[n + r] = sum
        return res


print Solution().longestConsecutive([9, 4, 6, 2, 1, 3])
