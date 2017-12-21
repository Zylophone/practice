# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.first, self.second, self.pre = None, None, None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.pre:
                if self.pre.val > root.val:
                    if not self.first:
                        self.first = self.pre
                    self.second = root
            self.pre = root
            inorder(root.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

node = TreeNode(0)
node.left = TreeNode(1)
print Solution().recoverTree(node)