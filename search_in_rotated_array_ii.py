class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return False
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return True

            if nums[mid] > nums[low]:
                if nums[mid] >= target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[low]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                low += 1
        return False


print Solution().search([3, 1, 1], 1)
