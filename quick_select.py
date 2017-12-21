class Solution(object):
    def select(self, nums, k):
        if len(nums) < k:
            return None
        p = nums[0]

        left, right = [], []
        for n in nums[1:]:
            if n < p:
                left.append(n)
            else:
                right.append(n)
        if len(left) == k - 1:
            return p
        elif len(left) > k - 1:
            return self.select(left, k)
        else:
            return self.select(right, k - len(left) - 1)
