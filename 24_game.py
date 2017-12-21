class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        diff = 0.01
        nums = map(float, nums)
        if len(nums) == 1:
            return abs(nums[0] - 24) < diff
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                rest = []
                for k in range(0, len(nums)):
                    if k == i or k == j:
                        continue
                    rest.append(nums[k])
                new_nums = [nums[i] + nums[j]] + rest
                if self.judgePoint24(new_nums):
                    return True

                new_nums = [nums[i] - nums[j]] + rest
                if self.judgePoint24(new_nums):
                    return True

                new_nums = [nums[j] - nums[i]] + rest
                if self.judgePoint24(new_nums):
                    return True

                new_nums = [nums[i] * nums[j]] + rest
                if self.judgePoint24(new_nums):
                    return True

                if nums[j] != 0:
                    new_nums = [nums[i] / nums[j]] + rest
                    if self.judgePoint24(new_nums):
                        return True

                if nums[i] != 0:
                    new_nums = [nums[j] / nums[i]] + rest
                    if self.judgePoint24(new_nums):
                        return True
        return False


print Solution().judgePoint24([4, 1, 8, 7])
