class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        size = len(nums)
        nsize = size - k + 1
        sums = [0] * nsize
        max_left = [0] * nsize
        max_right = [0] * nsize
        total = 0
        for x in range(size):
            total += nums[x]
            if x >= k - 1:
                sums[x - k + 1] = total
                total -= nums[x - k + 1]

        m, idx = 0, 0
        for i in range(nsize):
            if sums[i] > m:
                m, idx = sums[i], i
            max_left[i] = (m, idx)
        m, idx = 0, 0
        for i in range(nsize - 1, -1, -1):
            if sums[i] > m:
                m, idx = sums[i], i
            max_right[i] = (m, idx)

        ans_sum = 0
        ans = []
        for i in range(k, nsize - k):
            va, ia = max_left[i - k]
            vb, ib = max_right[i + k]
            s = va + sums[i] + vb
            if s > ans_sum:
                ans = [ia, i, ib]
                ans_sum = s
        return ans


print Solution().maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)
