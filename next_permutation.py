class Solution(object):
    def nextPermutation(self, nums):
        idx = len(nums) - 1
        while idx > 0:
            if nums[idx] > nums[idx - 1]:
                break
            idx -= 1
        if idx == 0:
            nums.reverse()
            return

        val = nums[idx - 1]
        j = len(nums) - 1
        while j > idx:
            if nums[j] > val:
                break
            j -= 1

        nums[idx - 1] = nums[j]
        nums[j] = val
        nums[idx:] = reversed(nums[idx:])
        return


nums = [1, 3, 2]
Solution().nextPermutation(nums)
print nums
