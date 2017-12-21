class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        res = ''.join(sorted([str(i) for i in nums], cmp=lambda x, y: cmp(x + y, y + x), reverse=True))
        return res.lstrip('0') or '0'
