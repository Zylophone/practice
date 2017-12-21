class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        s = []
        for i in range(0, n * 2):
            num = nums[i % n]
            while s and nums[s[-1]] < num:
                res[s.pop()] = num

            if i < n:
                s.append(i)
        return res


print Solution().nextGreaterElements([1, 2, 1])
