class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0 for _ in range(0, len(nums))] for _ in range(0, len(nums))]
        for k in range(2, len(nums)):
            for l in range(0, len(nums) - 2):
                r = l + k
                if r >= len(nums):
                    break
                for m in range(l + 1, r):
                    dp[l][r] = max(dp[l][r], nums[l] * nums[m] * nums[r] + dp[l][m] + dp[m][r])
        return dp[0][len(nums) - 1]


print Solution().maxCoins([3, 1, 5, 8])
