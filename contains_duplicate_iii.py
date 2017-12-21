class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0:
            return False
        d = {}
        w = t + 1
        for i in range(len(nums)):
            slot = nums[i] / w
            if slot in d:
                return True
            if slot - 1 in d and abs(d[slot - 1] - nums[i]) <= t:
                return True
            if slot + 1 in d and abs(d[slot + 1] - nums[i]) <= t:
                return True
            d[slot] = nums[i]
            if i > k:
                del d[nums[i - k] / w]
        return False
