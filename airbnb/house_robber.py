class Solution(object):
    def max_result(self, nums):
        last, current = 0, 0
        for i in nums:
            tmp = max(last + i, current)
            last = current
            current = tmp
        return current

print Solution().max_result([5,1, 2, 6, 20, 2])