class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = []
        for i in range(0, k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                res = max(res, self.merge(self.getMax(nums1, i), self.getMax(nums2, k - i)))
        return res

    def getMax(self, nums, t):
        ans = []
        size = len(nums)
        for i in range(size):
            while ans and nums[i] > ans[-1] and t - len(ans) < size - i:
                ans.pop()
            if len(ans) < t:
                ans.append(nums[i])
        return ans

    def merge(self, nums1, nums2):
        n = []
        while nums1 or nums2:
            if nums1 > nums2:
                n.append(nums1[0])
                nums1 = nums1[1:]
            else:
                n.append(nums2[0])
                nums2 = nums2[1:]
        if nums1:
            n += nums1
        else:
            n += nums2
        return n




print Solution().getMax([9, 1, 2, 5, 8, 3], 3)