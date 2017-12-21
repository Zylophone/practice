class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        l = 0
        node = root
        while node.left:
            l += 1
            node = node.left

        r = 0
        node = root
        while node.right:
            r += 1
            node = node.right

        if l == r:
            return (1 << (l + 1)) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)