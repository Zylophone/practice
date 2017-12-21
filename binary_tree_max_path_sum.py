# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max = [root.val]
        self.get_max_sum(root, max)
        return max[0]

    def get_max_sum(self, node, g_max):
        if node.left:
            max_left = self.get_max_sum(node.left, g_max)
        else:
            max_left = 0
        if node.right:
            max_right = self.get_max_sum(node.right, g_max)
        else:
            max_right = 0
        g_max[0] = max(g_max[0], max_left + node.val, max_right + node.val, max_left + max_right + node.val)
        return node.val + max(max_left, max_right, 0)
