class Solution():
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[low]:
                if nums[mid] > target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


print Solution().search([3, 4, 4, 4, 4, 5, 0, 1, 2], 1)
