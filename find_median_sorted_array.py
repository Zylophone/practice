class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1) + len(nums2)
        if m % 2 == 0:
            return float((self.findK(nums1, nums2, (m + 1) / 2)) + self.findK(nums1, nums2, (m + 2) / 2)) / 2

        return self.findK(nums1, nums2, m / 2 + 1)

    def findK(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)

        if m > n:
            return self.findK(nums2, nums1, k)

        if m == 0:
            return nums2[k - 1]

        if k == 1:
            return min(nums1[0], nums2[0])

        i, j = min(k / 2, m), min(k / 2, n)

        if nums1[i - 1] > nums2[j - 1]:
            return self.findK(nums1, nums2[j:], k - j)
        else:
            return self.findK(nums1[i:], nums2, k - i)


print Solution().findMedianSortedArrays([1, 3], [2])
