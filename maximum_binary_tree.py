class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        num, idx = self.get_max(nums)
        node = TreeNode(num)
        node.left = self.constructMaximumBinaryTree(nums[:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx + 1:])
        return node

    def get_max(self, nums):
        ans, idx = nums[0], 0
        for i, num in enumerate(nums):
            if ans < num:
                ans, idx = num, i
        return ans, idx


print Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
