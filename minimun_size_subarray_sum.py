class Solution(object):
    def minSubArrayLen(self, s, nums):
        if len(nums) == 0:
            return 0
        i, j = 0, 0
        cnt = 0
        l = 1e9
        while i < len(nums):
            cnt += nums[i]

            while cnt >= s and i >= j:
                l = min(l, i - j + 1)
                cnt -= nums[j]
                j += 1

            i += 1
        return l if l != 1e9 else 0


print Solution().minSubArrayLen(11, [1, 2, 3, 4, 5])
