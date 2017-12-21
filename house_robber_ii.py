class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(n):
            last, now = 0, 0
            for i in n:
                tmp = now
                now = max(now, last + i)
                last = tmp
            return now

        return max(helper(nums[1:]), helper(nums[0:-1]))
