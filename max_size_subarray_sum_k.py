class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sum_to_idx = {}
        res = 0
        for i in range(len(nums)):
            count += nums[i]
            if count == k:
                res = max(res, i + 1)

            diff = count - k
            if diff in sum_to_idx:
                idx = sum_to_idx[diff]
                res = max(i - idx, res)

            if count not in sum_to_idx:
                sum_to_idx[count] = i
        return res


print Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3)
