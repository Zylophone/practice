class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        size = 0
        tails = [0] * len(nums)
        for num in nums:
            start, end = 0, size
            while start != end:
                mid = (start + end) / 2
                if tails[mid] < num:
                    start = mid + 1
                else:
                    end = mid
            tails[start] = num
            size = max(start + 1, size)
        return size


print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
